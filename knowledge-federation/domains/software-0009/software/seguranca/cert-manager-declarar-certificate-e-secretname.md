---
id: software.seguranca.tranche19.001841
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

# cert-manager: Declarar Certificate e secretName

## Em uma frase
**cert-manager — Declarar Certificate e secretName:** Um recurso Certificate descreve nomes, issuer e Secret de destino para o certificado gerenciado.

## Por que importa
O recorte de **declarar certificate e secretname** ajuda a automatizar ciclo de vida de certificados TLS com configuração declarativa e integração a workloads. A equipe registra risco, evidência e responsável.

## Como funciona
Para **declarar certificate e secretname**, Certificate referencia Issuer ou ClusterIssuer; o controller solicita certificado, grava Secret e acompanha renovação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Crie Certificate de domínio de staging e confira que o Secret é criado no mesmo namespace. Teste em staging autorizado.

## Limites e trade-offs
Certificate Ready não comprova que ingress externo está servindo o Secret esperado. Exceções exigem responsável e prazo.

## Como verificar
Inspecione status, SANs, issuer e serial e conecte cliente ao endpoint de teste. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cert-manager-escolher-issuer-ou-clusterissuer]] — Complementa o tópico com cert-manager: escolher issuer ou clusterissuer.

## Fontes
- [cert-manager — Certificate usage](https://cert-manager.io/docs/usage/certificate/) — guia oficial de recursos Certificate, issuerRef, Secret e renovação; consultado em 2026-10-04.
- [cert-manager — Issuers](https://cert-manager.io/docs/configuration/issuers/) — documentação oficial de Issuer, ClusterIssuer e tipos de autoridade; consultado em 2026-10-04.
