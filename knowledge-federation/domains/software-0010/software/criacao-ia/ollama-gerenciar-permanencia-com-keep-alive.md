---
id: software.criacao_ia.tranche02.000116
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: ["https://docs.continue.dev/customize/config", "https://github.com/ollama/ollama/blob/main/docs/api.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ollama: gerenciar permanência na VRAM com keep_alive

## Em uma frase
O controle do parâmetro keep_alive define quanto tempo um modelo de linguagem permanece carregado na memória GPU após uma requisição.

## Por que importa
Descarregar o modelo a cada chamada causa travamentos frequentes na IDE pelo tempo de re-leitura do arquivo binário do disco para a memória.

## Como funciona
Defina `keep_alive` como um intervalo temporal (ex.: `30m`) nas requisições da API ou configure a variável de ambiente `OLLAMA_KEEP_ALIVE` para reter o modelo na VRAM entre edições contínuas de código.

## Exemplo
```bash
# Executar chamada de inferencia com permanencia de 30 minutos na VRAM
curl http://localhost:11434/api/generate -d '{
  "model": "qwen2.5-coder:7b",
  "prompt": "// Funcao de conversao de coordenadas",
  "keep_alive": "30m"
}'
```

## Limites e trade-offs
Manter múltiplos modelos em memória simultaneamente pode saturar a VRAM e causar falhas em aplicações gráficas e engines de jogos abertas paralelamente.

## Como verificar
Execute `ollama ps` no terminal para verificar quais modelos estão alocados na GPU e o tempo restante antes do descarregamento automático.

## Conexões
- [[ollama-ajustar-num-ctx-e-quantizacao-gguf]] — Veja também: Ollama: ajustar num_ctx e quantização GGUF para estabilidade de memória.
- [[llamacpp-servir-endpoint-openai-compativel]] — Veja também: llama.cpp: servir endpoint HTTP compatível com OpenAI.
- [[continue-dev-configurar-provedor-local]] — Conexão temática direta com continue-dev-configurar-provedor-local.

## Fontes
- [Continue.dev Documentation — Configuration Reference](https://docs.continue.dev/customize/config) — Documentação oficial de configuração do config.json, provedores de modelos locais e context providers. Consulta: 2026-10-04.
- [Ollama API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md) — Especificação oficial dos endpoints de inferência, parâmetros num_ctx, keep_alive e quantização gguf. Consulta: 2026-10-04.
