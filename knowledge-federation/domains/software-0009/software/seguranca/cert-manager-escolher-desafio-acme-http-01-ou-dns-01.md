---
id: software.seguranca.tranche19.001845
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

# cert-manager: Escolher desafio ACME HTTP-01 ou DNS-01

## Em uma frase
**cert-manager — Escolher desafio ACME HTTP-01 ou DNS-01:** Issuers ACME podem validar controle do domínio por desafios HTTP-01 ou DNS-01 conforme solver configurado.

## Por que importa
O recorte de **escolher desafio acme http-01 ou dns-01** ajuda a automatizar ciclo de vida de certificados TLS com configuração declarativa e integração a workloads. A equipe registra risco, evidência e responsável.

## Como funciona
Para **escolher desafio acme http-01 ou dns-01**, Certificate referencia Issuer ou ClusterIssuer; o controller solicita certificado, grava Secret e acompanha renovação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use DNS-01 para domínio wildcard em zona de teste e limite credencial DNS à zona necessária. Teste em staging autorizado.

## Limites e trade-offs
Credencial do solver com escopo amplo pode alterar registros fora do domínio do certificado. Exceções exigem responsável e prazo.

## Como verificar
Valide challenge, record temporário e limpeza após emissão em uma zona descartável. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cert-manager-configurar-renovacao-antecipada]] — Complementa o tópico com cert-manager: configurar renovação antecipada.

## Fontes
- [cert-manager — Certificate usage](https://cert-manager.io/docs/usage/certificate/) — guia oficial de recursos Certificate, issuerRef, Secret e renovação; consultado em 2026-10-04.
- [cert-manager — Issuers](https://cert-manager.io/docs/configuration/issuers/) — documentação oficial de Issuer, ClusterIssuer e tipos de autoridade; consultado em 2026-10-04.
