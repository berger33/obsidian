---
id: software.criacao_ia.tranche02.000114
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

# Continue.dev: separar modelo de autocomplete Tab do modelo de chat

## Em uma frase
A separação entre modelos de preenchimento inline e modelos de chat otimiza a latência e a qualidade da assistência na digitação.

## Por que importa
O autocomplete por Tab requer respostas em menos de 100 milissegundos, enquanto diálogos e refatorações toleram modelos maiores e mais lentos.

## Como funciona
No `config.json`, configure o campo `tabAutocompleteModel` com um modelo ultrarrápido otimizado para Fill-in-the-Middle (FIM) como `qwen2.5-coder:1.5b-base`, mantendo um modelo maior para o chat principal.

## Exemplo
```json
{
  "tabAutocompleteModel": {
    "title": "StarCoder2 3B",
    "provider": "ollama",
    "model": "starcoder2:3b"
  }
}
```

## Limites e trade-offs
Modelos de autocomplete não instrucionais geram repetições de código se os parâmetros de prefixo e sufixo FIM estiverem descalibrados.

## Como verificar
Abra um arquivo de código, inicie a declaração de uma função comum e avalie se as sugestões inline em cinza surgem de maneira instantânea e coerente.

## Conexões
- [[continue-dev-customizar-context-providers]] — Veja também: Continue.dev: customizar context providers para documentação.
- [[ollama-ajustar-num-ctx-e-quantizacao-gguf]] — Veja também: Ollama: ajustar num_ctx e quantização GGUF para estabilidade de memória.
- [[continue-dev-configurar-provedor-local]] — Conexão temática direta com continue-dev-configurar-provedor-local.
- [[copilot-prompts-com-criterios-de-aceitacao]] — Conexão temática direta com copilot-prompts-com-criterios-de-aceitacao.

## Fontes
- [Continue.dev Documentation — Configuration Reference](https://docs.continue.dev/customize/config) — Documentação oficial de configuração do config.json, provedores de modelos locais e context providers. Consulta: 2026-10-04.
- [Ollama API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md) — Especificação oficial dos endpoints de inferência, parâmetros num_ctx, keep_alive e quantização gguf. Consulta: 2026-10-04.
