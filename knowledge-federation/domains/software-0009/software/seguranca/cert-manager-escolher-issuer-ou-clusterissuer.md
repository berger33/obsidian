---
id: software.seguranca.tranche19.001842
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

# cert-manager: Escolher Issuer ou ClusterIssuer

## Em uma frase
**cert-manager — Escolher Issuer ou ClusterIssuer:** Issuer opera no namespace correspondente; ClusterIssuer pode ser referenciado por recursos de outros namespaces.

## Por que importa
O recorte de **escolher issuer ou clusterissuer** ajuda a automatizar ciclo de vida de certificados TLS com configuração declarativa e integração a workloads. A equipe registra risco, evidência e responsável.

## Como funciona
Para **escolher issuer ou clusterissuer**, Certificate referencia Issuer ou ClusterIssuer; o controller solicita certificado, grava Secret e acompanha renovação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use Issuer namespaced para certificado de aplicação que não precisa de autoridade global. Teste em staging autorizado.

## Limites e trade-offs
ClusterIssuer amplia alcance e pode compartilhar credencial ou policy entre equipes. Exceções exigem responsável e prazo.

## Como verificar
Confira namespace, referência e permissões do solver antes de aceitar emissão. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cert-manager-usar-referencia-explicita-de-issuer]] — Complementa o tópico com cert-manager: usar referência explícita de issuer.

## Fontes
- [cert-manager — Certificate usage](https://cert-manager.io/docs/usage/certificate/) — guia oficial de recursos Certificate, issuerRef, Secret e renovação; consultado em 2026-10-04.
- [cert-manager — Issuers](https://cert-manager.io/docs/configuration/issuers/) — documentação oficial de Issuer, ClusterIssuer e tipos de autoridade; consultado em 2026-10-04.
