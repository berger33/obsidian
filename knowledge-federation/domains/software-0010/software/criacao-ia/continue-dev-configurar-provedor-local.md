---
id: software.criacao_ia.tranche02.000111
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

# Continue.dev: configurar provedores locais no config.json

## Em uma frase
A extensão Continue permite acoplar modelos open-source executados localmente através do arquivo config.json da IDE.

## Por que importa
Utilizar inferência local garante privacidade de código confidencial e elimina custos recorrentes de chamadas de API externas durante o desenvolvimento.

## Como funciona
No arquivo de configuração `config.json` do Continue, declare uma entrada no array `models` com o provider `ollama` ou `openai` apontando para o endpoint local `http://localhost:11434/v1` com o identificador do modelo baixado.

## Exemplo
```json
{
  "models": [
    {
      "title": "Qwen 2.5 Coder 7B",
      "provider": "ollama",
      "model": "qwen2.5-coder:7b",
      "apiBase": "http://localhost:11434"
    }
  ]
}
```

## Limites e trade-offs
Modelos locais de pequeno porte têm janelas de contexto limitadas e capacidade de raciocínio inferior a modelos de fronteira em refatorações extensas.

## Como verificar
Abra a interface lateral do Continue no editor, selecione o modelo local recém-adicionado e envie uma pergunta sobre o arquivo aberto para verificar a resposta da GPU.

## Conexões
- [[continue-dev-indexar-codebase-com-embeddings-locais]] — Veja também: Continue.dev: indexar codebase com embeddings locais.
- [[ia-local-garantir-isolamento-sem-conexao-externa]] — Conexão temática direta com ia-local-garantir-isolamento-sem-conexao-externa.
- [[ollama-ajustar-num-ctx-e-quantizacao-gguf]] — Conexão temática direta com ollama-ajustar-num-ctx-e-quantizacao-gguf.
- [[continue-dev-separar-modelo-de-autocomplete-tab]] — Conexão temática direta com continue-dev-separar-modelo-de-autocomplete-tab.

## Fontes
- [Continue.dev Documentation — Configuration Reference](https://docs.continue.dev/customize/config) — Documentação oficial de configuração do config.json, provedores de modelos locais e context providers. Consulta: 2026-10-04.
- [Ollama API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md) — Especificação oficial dos endpoints de inferência, parâmetros num_ctx, keep_alive e quantização gguf. Consulta: 2026-10-04.
