mkdir -p ~/.streamlit/

echo"\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headles s = true\n
\n\
" > ~/.streamlit/config.toml
