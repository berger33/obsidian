---
id: software.seguranca.tranche19.001848
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

# cert-manager: Selecionar solver pelo domínio

## Em uma frase
**cert-manager — Selecionar solver pelo domínio:** Configuração do issuer pode escolher solver por zona, selector e características do nome solicitado.

## Por que importa
O recorte de **selecionar solver pelo domínio** ajuda a automatizar ciclo de vida de certificados TLS com configuração declarativa e integração a workloads. A equipe registra risco, evidência e responsável.

## Como funciona
Para **selecionar solver pelo domínio**, Certificate referencia Issuer ou ClusterIssuer; o controller solicita certificado, grava Secret e acompanha renovação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Separe zonas de staging e produção com seletores e credenciais diferentes. Teste em staging autorizado.

## Limites e trade-offs
Selector ambíguo pode enviar desafio a conta DNS incorreta. Exceções exigem responsável e prazo.

## Como verificar
Emita certificado de cada zona de teste e inspecione solver e identidade usada. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cert-manager-investigar-falhas-sem-expor-credenciais]] — Complementa o tópico com cert-manager: investigar falhas sem expor credenciais.

## Fontes
- [cert-manager — Certificate usage](https://cert-manager.io/docs/usage/certificate/) — guia oficial de recursos Certificate, issuerRef, Secret e renovação; consultado em 2026-10-04.
- [cert-manager — Issuers](https://cert-manager.io/docs/configuration/issuers/) — documentação oficial de Issuer, ClusterIssuer e tipos de autoridade; consultado em 2026-10-04.
