# dagpt

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

A short description of the project.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         src and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── src   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

# Hướng Dẫn Xây Dựng Công Cụ Trợ Giúp Phân Tích Dữ Liệu (DAGPT)
## Giới Thiệu
Chào mừng bạn đến với kênh Data Science Lab! Trong video này, mình sẽ cùng với bạn xây dựng một công cụ phân tích dữ liệu hữu ích và tiện lợi tên là DAGPT (Data Analysis GPT). Công cụ này sử dụng các mô hình ngôn ngữ lớn (LLMs) để hỗ trợ việc thao tác và phân tích dữ liệu thông qua giao diện đàm thoại. Dự án này sử dụng Python, Langchain, Streamlit, PyGWalker, OpenAI API để tạo ra một ứng dụng web tương tác, cho phép người dùng tải lên dữ liệu, đặt câu hỏi, khám phá dữ liệu và nhận được các phân tích chi tiết.

# Nội Dung Video
## 1. Giới Thiệu về DAGPT
* Tổng quan: DAGPT là một công cụ phân tích dữ liệu sử dụng các mô hình ngôn ngữ lớn để hỗ trợ các tác vụ phân tích và thao tác dữ liệu qua giao diện đàm thoại.
* Tính năng:
  - Tải lên tệp CSV: Dễ dàng tải lên dữ liệu CSV qua thanh bên.
  - Phân tích dữ liệu: Nhập các truy vấn về dữ liệu và nhận phản hồi được hỗ trợ bởi LLMs.
  - Trực quan hóa dữ liệu: Tạo và hiển thị các biểu đồ dựa trên các truy vấn dữ liệu.
  - Công cụ trực quan hóa tương tác: Khám phá dữ liệu một cách tương tác bằng cách sử dụng các biểu đồ tùy chỉnh.