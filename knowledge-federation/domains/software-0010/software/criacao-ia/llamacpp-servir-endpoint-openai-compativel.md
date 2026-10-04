---
id: software.criacao_ia.tranche02.000117
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

# llama.cpp: servir endpoint HTTP compatível com OpenAI

## Em uma frase
O binário llama-server expõe uma API REST de alta performance compatível com ferramentas que consomem o padrão da OpenAI.

## Por que importa
O llama.cpp oferece suporte direto a aceleração por GPU (CUDA, Metal, Vulkan) e processamento contínuo em lote (*continuous batching*).

## Como funciona
Inicie o `llama-server` informando o arquivo `.gguf`, a porta TCP de escuta e o número de camadas a descarregar na GPU (`-ngl`). Aponte o assistente de desenvolvimento para o endpoint `http://localhost:8080/v1`.

## Exemplo
```bash
# Iniciar o servidor HTTP do llama.cpp com aceleracao GPU
./llama-server   -m models/qwen2.5-coder-7b-instruct-q5_k_m.gguf   -c 8192   -ngl 99   --port 8080   --host 127.0.0.1
```

## Limites e trade-offs
Parâmetros incorretos de threads de CPU ou camadas de GPU podem causar lentidão severa ou erros de alocação de memória na inicialização do servidor.

## Como verificar
Faça uma requisição HTTP `POST /v1/chat/completions` com cURL e confirme a recepção do stream de tokens e a medição do tempo de primeiro token.

## Conexões
- [[ollama-gerenciar-permanencia-com-keep-alive]] — Veja também: Ollama: gerenciar permanência na VRAM com keep_alive.
- [[continue-dev-padronizar-regras-de-projeto]] — Veja também: Continue.dev: padronizar regras de projeto e system prompts.
- [[continue-dev-configurar-provedor-local]] — Conexão temática direta com continue-dev-configurar-provedor-local.
- [[ia-local-garantir-isolamento-sem-conexao-externa]] — Conexão temática direta com ia-local-garantir-isolamento-sem-conexao-externa.

## Fontes
- [Continue.dev Documentation — Configuration Reference](https://docs.continue.dev/customize/config) — Documentação oficial de configuração do config.json, provedores de modelos locais e context providers. Consulta: 2026-10-04.
- [Ollama API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md) — Especificação oficial dos endpoints de inferência, parâmetros num_ctx, keep_alive e quantização gguf. Consulta: 2026-10-04.
