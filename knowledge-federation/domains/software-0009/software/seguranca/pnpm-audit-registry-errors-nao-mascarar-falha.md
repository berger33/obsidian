---
id: software.seguranca.tranche17.001658
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://pnpm.io/cli/audit#--ignore-registry-errors", "https://pnpm.io/settings/dependency-resolution#registries"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `--ignore-registry-errors`: não confundir indisponibilidade do serviço com resultado limpo

## Em uma frase
A opção `--ignore-registry-errors` pode fazer o processo retornar zero quando o registry responde com status não 200, separando falha do serviço de achados.

## Por que importa
Mascarar indisponibilidade como sucesso pode deixar uma janela sem auditoria sem que a equipe perceba; observabilidade de falhas precisa continuar explícita.

## Como funciona
Use essa opção somente em fluxos que registram erro de consulta por outro canal, e mantenha uma métrica ou estado de auditoria inconclusa.

## Exemplo
Se o job não puder falhar a release por outage, publique o status `audit inconclusiva`, abra alerta operacional e agende nova tentativa em vez de marcar `clean`.

## Limites e trade-offs
Código de saída zero nessa opção não significa que o registry consultado confirmou ausência de vulnerabilidades.

## Como verificar
Simule erro HTTP, confira status do comando e verifique que o pipeline mostra auditoria inconclusiva sem suprimir a falha de serviço.

## Conexões
- [[pnpm-audit-level-impressao-severidade-policy]] — `--audit-level` no pnpm: controlar severidade exibida sem perder dados brutos.
- [[pnpm-audit-signatures-registry-ecdsa-chaves]] — `pnpm audit signatures`: verificar assinaturas ECDSA do registry instalado.

## Fontes
- [pnpm — `--ignore-registry-errors`](https://pnpm.io/cli/audit#--ignore-registry-errors) — efeito de erros do registry sobre o status de saída; consultado em 2026-10-04.
- [pnpm — registries configurados](https://pnpm.io/settings/dependency-resolution#registries) — seleção e configuração dos registries dos quais dependem consultas de advisory; consultado em 2026-10-04.
