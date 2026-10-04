---
id: software.criacao_ia.tranche03.000223
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
fontes: ["https://openai.github.io/openai-agents-python/handoffs/#handoff-inputs", "https://openai.github.io/openai-agents-python/context/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Agents SDK: validar handoff input em on_handoff

## Em uma frase
Quando autorização depende de campos gerados pelo modelo no handoff, valide o payload no início de `on_handoff`, antes de efeitos colaterais.

## Por que importa
`is_enabled` decide se a rota fica disponível antes que o modelo produza os argumentos e por isso não pode autorizar valores específicos desses argumentos. Além disso, tool input guardrails do SDK não abrangem handoffs, apesar de o handoff ser apresentado ao modelo como uma espécie de tool.

## Como funciona
Use `input_type` para descrever e validar localmente o JSON do handoff; o SDK converte-o para schema e passa o valor analisado ao callback. Em `on_handoff`, verifique identidade, limites e política de negócio antes de reservar recursos ou iniciar ações. Ao falhar, levante erro em vez de retornar normalmente, pois retorno bem-sucedido deixa o runtime continuar a transferência. Dados de dependência já conhecidos ficam em `RunContextWrapper.context`, não em argumentos que o modelo inventa.

## Exemplo
Um agente pede escalonamento com campos `reason` e `priority`. `on_handoff` confirma que o usuário pode encaminhar aquela categoria, grava um evento idempotente e só depois autoriza o agente receptor. Uma prioridade `critical` isolada não eleva privilégios apenas porque passou a validação de tipo.

## Limites e trade-offs
Validação Pydantic ou JSON verifica estrutura, não autorização substantiva. A aplicação precisa considerar repetição, concorrência e falha parcial do callback. Outros caminhos para invocar a operação devem aplicar a mesma regra.

## Como verificar
Teste enumerações inválidas, usuário sem permissão, callback que lança exceção e execução repetida. Confirme que nenhum serviço externo foi chamado antes da decisão e que `is_enabled` não é usado como única checagem de argumentos.

## Conexões
- [[agents-sdk-handoff-destino-fixo]] — Agents SDK handoff: modelar destinos como roteamento explícito.
- [[agents-sdk-guardrails-fronteiras-primeiro-e-ultimo-agente]] — Agents SDK guardrails: mapear fronteiras de primeiro e último agente.

## Fontes
- [OpenAI Agents SDK — Handoff inputs](https://openai.github.io/openai-agents-python/handoffs/#handoff-inputs) — explica schema, momento de `is_enabled` e validação no callback antes de side effects Consulta: 2026-10-04.
- [OpenAI Agents SDK — Context management](https://openai.github.io/openai-agents-python/context/) — distingue dados locais de contexto de argumentos que o modelo fornece Consulta: 2026-10-04.
