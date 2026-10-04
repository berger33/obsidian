---
id: software.criacao_ia.tranche02.000113
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

# Continue.dev: customizar context providers para documentação

## Em uma frase
Os context providers do Continue permitem injetar documentações externas, issues e arquivos específicos no prompt do assistente.

## Por que importa
Fornecer referências precisas de frameworks reduz o risco de uso de métodos obsoletos ou sintaxe incorreta gerada pelo modelo.

## Como funciona
Utilize identificadores de contexto como `@docs` apontando para URLs indexadas ou adicione providers customizados em TypeScript no diretório `.continue/rules` para carregar esquemas de banco de dados e diagramas.

## Exemplo
```json
{
  "docs": [
    {
      "title": "Godot 4 Docs",
      "startUrl": "https://docs.godotengine.org/en/stable/",
      "rootUrl": "https://docs.godotengine.org/en/stable/"
    }
  ]
}
```

## Limites e trade-offs
A indexação excessiva de páginas web de documentação pode poluir a base vetorial com seções de introdução e menus de navegação.

## Como verificar
Acione `@docs Godot 4 Docs CharacterBody3D` no chat e examine se os trechos de texto recuperados correspondem à documentação oficial do nó.

## Conexões
- [[continue-dev-indexar-codebase-com-embeddings-locais]] — Veja também: Continue.dev: indexar codebase com embeddings locais.
- [[continue-dev-separar-modelo-de-autocomplete-tab]] — Veja também: Continue.dev: separar modelo de autocomplete Tab do modelo de chat.
- [[cursor-usar-simbolos-de-contexto-docs-e-git]] — Conexão temática direta com cursor-usar-simbolos-de-contexto-docs-e-git.
- [[diataxis-organizar-referencias-tecnicas-sem-narrativa]] — Conexão temática direta com diataxis-organizar-referencias-tecnicas-sem-narrativa.

## Fontes
- [Continue.dev Documentation — Configuration Reference](https://docs.continue.dev/customize/config) — Documentação oficial de configuração do config.json, provedores de modelos locais e context providers. Consulta: 2026-10-04.
- [Ollama API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md) — Especificação oficial dos endpoints de inferência, parâmetros num_ctx, keep_alive e quantização gguf. Consulta: 2026-10-04.
