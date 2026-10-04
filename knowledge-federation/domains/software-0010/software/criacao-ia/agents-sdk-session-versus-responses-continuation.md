---
id: software.criacao_ia.tranche03.000226
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
fontes: ["https://openai.github.io/openai-agents-python/sessions/", "https://openai.github.io/openai-agents-python/running_agents/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Agents SDK: escolher session local ou continuação server-side

## Em uma frase
Uma Session gerencia histórico local do Agents SDK e não pode ser combinada no mesmo run com `conversation_id`, `previous_response_id` ou `auto_previous_response_id`.

## Por que importa
Empilhar dois mecanismos de conversa pode duplicar mensagens, produzir histórico divergente e dificultar a exclusão de dados. Uma sessão local e continuação no servidor mantêm estado em camadas e com regras de retenção diferentes.

## Como funciona
Escolha Session quando o SDK deve recuperar e salvar itens de conversa no backend configurado. Escolha uma das opções de continuação da Responses API quando o estado server-side for desejado; reenvie somente a nova entrada conforme esse mecanismo. Para runs pausados por aprovação, retome com a mesma instância ou um objeto configurado com o mesmo session ID e backend.

## Exemplo
Uma ferramenta desktop usa `SQLiteSession` no ambiente local durante múltiplos turnos e configura limites de histórico. Um serviço que usa `previous_response_id` na Responses API guarda esse ID e não passa Session ao mesmo run; sua política de dados cobre separadamente estado remoto e registros locais.

## Limites e trade-offs
Session mantém itens e histórico segundo o backend e configuração escolhidos, mas não é por si só uma política de retenção ou autorização. A documentação descreve mecanismos incompatíveis no mesmo run; não deduza que duas execuções independentes não possam migrar entre mecanismos com transformação explícita.

## Como verificar
Adicione um teste que tente misturar cada par de mecanismos e espere falha de configuração. Confirme retomada de aprovação com mesmo storage, limite de itens recuperados e comportamento após reinício do processo.

## Conexões
- [[agents-sdk-streaming-drenar-ate-fim]] — Agents SDK streaming: consumir eventos até o iterador terminar.
- [[agents-sdk-output-type-e-handoffs]] — Agents SDK: normalizar saída tipada entre handoffs.

## Fontes
- [OpenAI Agents SDK — Sessions](https://openai.github.io/openai-agents-python/sessions/) — declara incompatibilidade no mesmo run com continuation options server-side Consulta: 2026-10-04.
- [OpenAI Agents SDK — Running agents](https://openai.github.io/openai-agents-python/running_agents/) — descreve opções de continuação e ciclo de execução do Runner Consulta: 2026-10-04.
