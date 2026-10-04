---
id: software.criacao_ia.tranche03.000222
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
fontes: ["https://openai.github.io/openai-agents-python/handoffs/", "https://openai.github.io/openai-agents-python/multi_agent/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Agents SDK handoff: modelar destinos como roteamento explícito

## Em uma frase
A função `handoff()` transfere sempre para o agente específico passado na configuração; não escolhe um destino diferente com base no texto gerado.

## Por que importa
Um fluxo de triagem com vários especialistas precisa expor ao modelo escolhas explícitas ou determinar o destino em código. Tratar um handoff como roteador dinâmico pode esconder caminhos possíveis e tornar pouco previsíveis os efeitos do callback de handoff.

## Como funciona
Registre um handoff separado para cada agente de destino e deixe o modelo selecionar entre eles quando o roteamento for parte do julgamento. Para lógica própria que precisa decidir o próximo agente durante a chamada, use a abstração customizada documentada. `input_type` descreve metadados produzidos pelo modelo para o handoff, mas não troca o agente de destino da função auxiliar.

## Exemplo
Um agente de triagem publica `transfer_to_billing` e `transfer_to_technical_support` como caminhos independentes, ambos com descrições curtas. Se a política interna exige que pedidos de reembolso acima de um limite usem um fluxo escolhido por código, a aplicação implementa um handoff customizado e valida esse limite antes de transferir.

## Limites e trade-offs
Descrições e nomes de tools guiam a decisão do modelo, mas não garantem classificação correta. Uma escolha de destino em código continua sujeita a validação de entrada, autorização e tratamento de exceções.

## Como verificar
Inspecione o conjunto de handoffs anunciado ao agente, force exemplos para cada rota e confirme o agente ativo depois da transferência. Teste argumentos ausentes, inválidos e casos fora das categorias previstas.

## Conexões
- [[agents-sdk-especialista-como-tool-ou-handoff]] — Agents SDK: escolher Agent.as_tool ou handoff.
- [[agents-sdk-on-handoff-autorizacao-antes-de-efeitos]] — Agents SDK: validar handoff input em on_handoff.

## Fontes
- [OpenAI Agents SDK — Handoffs](https://openai.github.io/openai-agents-python/handoffs/) — define destino fixo e recomenda um handoff registrado por destino possível Consulta: 2026-10-04.
- [OpenAI Agents SDK — Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/) — posiciona handoff como roteamento que torna o especialista o agente ativo Consulta: 2026-10-04.
