---
id: software.seguranca.tranche19.001843
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-19.md"
fontes: ["https://cert-manager.io/docs/usage/certificate/", "https://cert-manager.io/docs/configuration/issuers/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# cert-manager: Usar referência explícita de issuer

## Em uma frase
**cert-manager — Usar referência explícita de issuer:** Certificate referencia issuer por nome e kind e pode nomear group para tipos externos.

## Por que importa
O recorte de **usar referência explícita de issuer** ajuda a automatizar ciclo de vida de certificados TLS com configuração declarativa e integração a workloads. A equipe registra risco, evidência e responsável.

## Como funciona
Para **usar referência explícita de issuer**, Certificate referencia Issuer ou ClusterIssuer; o controller solicita certificado, grava Secret e acompanha renovação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Registre kind e nome do issuer na mesma revisão que cria o Certificate. Teste em staging autorizado.

## Limites e trade-offs
Nome errado ou issuer ausente deixa recurso pendente ou pode selecionar autoridade indevida. Exceções exigem responsável e prazo.

## Como verificar
Compare issuerRef com recurso existente e acompanhe condição e eventos do controller. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cert-manager-entender-status-e-condicoes-de-emissao]] — Complementa o tópico com cert-manager: entender status e condições de emissão.

## Fontes
- [cert-manager — Certificate usage](https://cert-manager.io/docs/usage/certificate/) — guia oficial de recursos Certificate, issuerRef, Secret e renovação; consultado em 2026-10-04.
- [cert-manager — Issuers](https://cert-manager.io/docs/configuration/issuers/) — documentação oficial de Issuer, ClusterIssuer e tipos de autoridade; consultado em 2026-10-04.
