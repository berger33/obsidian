---
id: software.criacao_ia.tranche02.000112
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

# Continue.dev: indexar codebase com embeddings locais

## Em uma frase
A indexação vetorial local viabiliza a recuperação de trechos relevantes do repositório através do provedor @codebase.

## Por que importa
Consultas baseadas em embeddings encontram definições de tipos, contratos e funções similares mesmo sem correspondência léxica exata nos nomes de variáveis.

## Como funciona
Configure um modelo de embedding local como `nomic-embed-text` no bloco `embeddingsProvider` do `config.json`. O Continue varre os arquivos do workspace, gera vetores e salva o índice em uma base SQLite com LanceDB local.

## Exemplo
```json
{
  "embeddingsProvider": {
    "provider": "ollama",
    "model": "nomic-embed-text"
  }
}
```

## Limites e trade-offs
O processo de indexação inicial consome recursos significativos de CPU e disco em repositórios muito volumosos sem arquivo de exclusão.

## Como verificar
Digite `@codebase onde está implementada a rotina de login?` no chat do Continue e valide se os arquivos retornados nos chunks coincidem com os módulos de autenticação.

## Conexões
- [[continue-dev-configurar-provedor-local]] — Veja também: Continue.dev: configurar provedores locais no config.json.
- [[continue-dev-customizar-context-providers]] — Veja também: Continue.dev: customizar context providers para documentação.
- [[cursor-otimizar-indexacao-com-cursorignore]] — Conexão temática direta com cursor-otimizar-indexacao-com-cursorignore.

## Fontes
- [Continue.dev Documentation — Configuration Reference](https://docs.continue.dev/customize/config) — Documentação oficial de configuração do config.json, provedores de modelos locais e context providers. Consulta: 2026-10-04.
- [Ollama API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md) — Especificação oficial dos endpoints de inferência, parâmetros num_ctx, keep_alive e quantização gguf. Consulta: 2026-10-04.
