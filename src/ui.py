import gradio as gr
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from .agent import WaferAgent
from .clustering import cluster_data
from .synthetic_data import generate_wafer_data
from .tools import WaferToolkit
load_dotenv(); toolkit=WaferToolkit(); agent=None; data=None
def initialize():
    global agent
    try: agent=WaferAgent(toolkit); return "Agent initialized."
    except Exception as e:return f"Initialization error: {e}"
def generate(count):
    global data
    data=generate_wafer_data(int(count)); toolkit.load(data); return data.head(10),f"Generated {len(data)} synthetic wafers."
def chat(message,history):
    if agent is None:return history+[(message,"Initialize the agent first.")]
    if data is None:return history+[(message,"Generate synthetic data first.")]
    try:return history+[(message,agent.ask(message))]
    except Exception as e:return history+[(message,f"Analysis error: {e}")]
def plot_clusters(k):
    if data is None:return None
    r=cluster_data(data,"kmeans",int(k)); fig,ax=plt.subplots(figsize=(8,5)); ax.scatter(r.coordinates[:,0],r.coordinates[:,1],c=r.labels,cmap="viridis",s=18); ax.set_title("PCA view of synthetic wafer clusters"); return fig
def create_interface():
    with gr.Blocks(title="Semiconductor AI Agent Workshop",theme=gr.themes.Soft()) as demo:
        gr.Markdown("""# Semiconductor AI Agent Workshop
Learn agentic AI with synthetic wafer data, tools, clustering, and a public OpenAI-compatible provider.""")
        with gr.Tab("Setup"):
            init=gr.Button("Initialize agent",variant="primary"); status=gr.Textbox(label="Status"); count=gr.Slider(100,2000,value=600,step=100,label="Synthetic wafer count"); create=gr.Button("Generate synthetic data"); table=gr.Dataframe(label="Preview",interactive=False,wrap=True,height=420); summary=gr.Textbox(label="Dataset status")
        with gr.Tab("Chat"):
            cb=gr.Chatbot(label="Conversation",height=420,type="tuples"); q=gr.Textbox(label="Question"); send=gr.Button("Send",variant="primary")
        with gr.Tab("Visualize"):
            k=gr.Slider(2,8,value=4,step=1,label="Cluster count"); viz=gr.Button("Create PCA cluster plot"); chart=gr.Plot()
        init.click(initialize,inputs=[],outputs=status); create.click(generate,inputs=count,outputs=[table,summary]); send.click(chat,inputs=[q,cb],outputs=cb).then(lambda:"",inputs=[],outputs=q); q.submit(chat,inputs=[q,cb],outputs=cb).then(lambda:"",inputs=[],outputs=q); viz.click(plot_clusters,inputs=k,outputs=chart)
    return demo
