# Chainlit Basics QA

#### Q1: How to upload a pdf file and load it for langchain?

```python
# demo codes
import tempfile
from langchain.document_loaders import PyPDFLoader

if action.value == 'upload_pdf_file':
    pdf_file = cl.ask_for_file(
        title='Upload a pdf file', accept=['application/pdf'], max_size_mb=10)

    temp_file = NamedTemporaryFile()
    temp_file.write(pdf_file.content)
    loader = PyPDFLoader(temp_file.name)

    documents = loader.load_and_split(text_splitter=text_splitter)
    content = documents[0].page_content

cl.send_message(content=content)
```

Key takeaways:

- using `cl.ask_for_file` function loading file
- specify `accept=['application/pdf']` to allow selection of pdf files only
- using _tempfile_ package to bridge cl.ask_for_file()) with pypdf
  - PyPDFLoader requires a file path, but chainlit only loads pdf to memory but not saves it to local folder.
  - `tempfile.write(pdf_file.content)` will save pdf content into a temp file with random name. With it assistance, pypdf now gets a path of tempfile for loading

#### Q2 How do the several langchain decorators work differently?

- `@lanchain_factory` wraps up a chain or agent of langchain and returns its object. Note that its decorated function doesn't send messages to UI
- `langchain_run(agent, prompt:TypedDict)` provides a chance of doing something before agent/chain runs a prompt. The prompt is a TypedDict with question & text two keys.
- `langchain_postprocess(message:TypedDict)` provides a chance to edit the output of agent/chain before it's sent to UI. If @langchain_run decorator is implemented, this postprocess decorator is not necessary for it can be the second part of run decorate following the execution of agent.

### Q3 Which element types are supposed in the current Chainlit?

Only Text and Image (LocalImage/RemoteImage).

`name=` property is used to expose elements as access point in side/page display (not affecting inline display)

#### Q4 Anything special with action_callback()?

- Action() class creates actions, whose `name=` property works like a class name, and `value=` property works like _id_ that differentiates multiple actions of same class. `label=` property is used to change text on the action link
- @action_callback takes one str parameter that specifies an action name
