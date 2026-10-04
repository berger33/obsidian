---
id: software.criacao_ia.tranche02.000115
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

# Ollama: ajustar num_ctx e quantização GGUF para estabilidade de memória

## Em uma frase
Dimensionar a janela de contexto (`num_ctx`) e a quantização do modelo evita estouro de VRAM na GPU durante a geração.

## Por que importa
Janelas de contexto padrão pequenas truncam arquivos longos, enquanto valores muito altos forçam o offloading para a RAM lenta do sistema.

## Como funciona
Ajuste o parâmetro `num_ctx` no Modelfile ou na requisição da API do Ollama e selecione quantizações equilibradas como Q4_K_M ou Q5_K_M para maximizar camadas carregadas na memória de vídeo dedicada.

## Exemplo
```dockerfile
# Exemplo de Modelfile customizado para aumentar o contexto no Ollama
FROM qwen2.5-coder:7b
PARAMETER num_ctx 16384
PARAMETER temperature 0.2
```

## Limites e trade-offs
Aumentar o `num_ctx` exige alocação proporcional de memória de atenção na GPU, reduzindo o espaço disponível para modelos auxiliares.

## Como verificar
Execute `ollama run meu-modelo-16k` e verifique com `nvidia-smi` ou `ollama ps` a quantidade de camadas (*layers*) acomodadas na VRAM.

## Conexões
- [[continue-dev-separar-modelo-de-autocomplete-tab]] — Veja também: Continue.dev: separar modelo de autocomplete Tab do modelo de chat.
- [[ollama-gerenciar-permanencia-com-keep-alive]] — Veja também: Ollama: gerenciar permanência na VRAM com keep_alive.
- [[continue-dev-configurar-provedor-local]] — Conexão temática direta com continue-dev-configurar-provedor-local.
- [[cursor-priorizar-janela-de-contexto-essencial]] — Conexão temática direta com cursor-priorizar-janela-de-contexto-essencial.

## Fontes
- [Continue.dev Documentation — Configuration Reference](https://docs.continue.dev/customize/config) — Documentação oficial de configuração do config.json, provedores de modelos locais e context providers. Consulta: 2026-10-04.
- [Ollama API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md) — Especificação oficial dos endpoints de inferência, parâmetros num_ctx, keep_alive e quantização gguf. Consulta: 2026-10-04.
