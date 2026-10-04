---
id: software.testes.tranche17.001059
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://docs.gatling.io/concepts/checks/", "https://github.com/gatling/gatling"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: validar respostas com checagens

## Em uma frase
As checagens avaliam cada resposta, como o código de status ou um campo do corpo, e registram falhas contabilizadas no relatório.

## Por que importa
Sem checagem, uma resposta de erro tratada como sucesso distorce o resultado do teste e esconde defeitos sob carga.

## Como funciona
Aplique checagens pontuais em cada requisição relevante, usando o campo que expressa o contrato, e trate falhas como falha do passo.

## Exemplo
Um passo de criação pode verificar o código de status e salvar o identificador devolvido para uso nas etapas seguintes.

## Limites e trade-offs
Checagens custam processamento no gerador e podem reduzir a taxa alcançada, então o custo precisa entrar na leitura do resultado.

## Como verificar
Altere o serviço de teste para devolver código inesperado e confirme que o relatório contabiliza a falha no passo correto.

## Conexões
- [[gatling-injection-profiles]] — Veja também: Gatling: escolher o perfil de injeção.
- [[gatling-session-and-extraction]] — Veja também: Gatling: transportar dados pela sessão.

## Fontes
- [Gatling — Checks](https://docs.gatling.io/concepts/checks/) — checagens de resposta, captura de valores e contabilização de falhas; consultado em 2026-10-03.
- [Gatling — repositório oficial](https://github.com/gatling/gatling) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
