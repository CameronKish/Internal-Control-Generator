# Sarbanes-Oxley (SOX) Compliant Accounting Internal Control Generation (under production)
Setting up a SOX compliant internal conrol environment is very challenging and requires a large amount of business expertise. Large public companies and pre-ipo businesses alike struggle with documenting and implementing internal controls. This project aims to give businesses an expert AI assistant that will help with docuemnting these complex controls with a simple interface. Additionally, this technology will leverage AI to allow users to ask questions about their current internal control environment so even newly hired employees can properly document processes they are responsible for. 

**Steps to build this project:**
- Utilize python speech to text and custom control form as input for private Ollama model (Llama2/Mistral)
- Embed text conversation and control form inputs into SQLite database via ChromaDB
- Define functions to super-prompt LLM with SOX compliant control attribute templates
- Design user interface via PySide6
- Ensure SOC 2 Type 2 compliant program along the way
