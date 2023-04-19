# Generate llama index file

    docker run --rm -e OPENAI_API_KEY=<OPENAI_API_KEY> gudaoco/llama:latest python3 ./gen.py <sourceDir> <indexFile.json>

# Run llama query http server

    docker run -e OPENAI_API_KEY=<OPENAI_API_KEY> -p 8080:8080 gudaoco/llama:latest
    
    curl -X POST "http://localhost:8080/v1/query.json" -d '{"body":"gudao.co?"}'

