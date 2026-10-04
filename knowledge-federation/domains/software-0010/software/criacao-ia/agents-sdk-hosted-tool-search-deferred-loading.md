---
id: software.criacao_ia.tranche03.000228
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://openai.github.io/openai-agents-python/tools/", "https://openai.github.io/openai-agents-python/streaming/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Agents SDK: adiar tool schemas com hosted tool search

## Em uma frase
Hosted tool search permite carregar sob demanda uma parte de um catálogo grande de tools em modelos OpenAI Responses compatíveis.

## Por que importa
Expor centenas de schemas em cada chamada aumenta tokens e pode diluir a seleção do modelo. Carregar namespaces quando necessários reduz o catálogo inicial, mas muda a forma como uma tool fica disponível e exige instrumentar os eventos de busca e retorno.

## Como funciona
Marque superfícies elegíveis como deferred loading e configure exatamente um `ToolSearchTool()` no agente. A documentação consultada indica suporte a OpenAI Responses models e dependência de `openai>=2.25.0` na integração Python. `tool_namespace()` agrupa funções relacionadas; client-executed tool search requer que a aplicação gerencie a busca e não é autoexecutada pelo `Runner` padrão.

## Exemplo
Um agente de produção agrupa funções `build`, `publish` e `rollback` sob namespace de deploy. Mantém busca e tools de leitura imediata expostas, enquanto ferramentas de deploy são carregadas somente quando o modelo identifica uma tarefa de publicação; os eventos `tool_search_called` ficam disponíveis para auditoria.

## Limites e trade-offs
A disponibilidade e os requisitos de versão mudam com SDK e provider. Busca adiada não é controle de acesso: valide permissões na execução de cada função e evite expor segredos apenas porque um namespace foi carregado.

## Como verificar
Fixe versões, confirme a presença de um único `ToolSearchTool`, verifique chamadas que precisam ou não de namespace e avalie tokens de schema. Teste modelo/provider não compatível e rejeição de uma tool por falta de permissão.

## Conexões
- [[agents-sdk-output-type-e-handoffs]] — Agents SDK: normalizar saída tipada entre handoffs.
- [[agents-sdk-session-input-callback-historico]] — Agents SDK Sessions: limitar histórico lido sem duplicar persistência.

## Fontes
- [OpenAI Agents SDK — Tools](https://openai.github.io/openai-agents-python/tools/) — documenta deferred loading, `ToolSearchTool`, limitações de provider e requisito de SDK Consulta: 2026-10-04.
- [OpenAI Agents SDK — Streaming](https://openai.github.io/openai-agents-python/streaming/) — define eventos de busca de tools para observabilidade do fluxo Consulta: 2026-10-04.
