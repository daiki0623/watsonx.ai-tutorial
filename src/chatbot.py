import gradio as gr
import model


def bot_response(message, history):
    return model.generate_text(message)


if __name__ == "__main__":
    demo = gr.ChatInterface(bot_response)
    demo.launch()
