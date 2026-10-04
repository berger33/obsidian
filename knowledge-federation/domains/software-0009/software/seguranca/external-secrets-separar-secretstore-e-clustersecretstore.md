---
id: software.seguranca.tranche19.001881
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
fontes: ["https://external-secrets.io/latest/provider/google-secrets-manager/", "https://github.com/external-secrets/external-secrets/blob/main/docs/api/clustersecretstore.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# External Secrets Operator: Separar SecretStore e ClusterSecretStore

## Em uma frase
**External Secrets Operator — Separar SecretStore e ClusterSecretStore:** SecretStore tem escopo namespaced; ClusterSecretStore pode ser referenciado por ExternalSecrets de vários namespaces.

## Por que importa
O recorte de **separar secretstore e clustersecretstore** ajuda a reduzir duplicação manual de credenciais e separar fonte de segredo das aplicações consumidoras. A equipe registra risco, evidência e responsável.

## Como funciona
Para **separar secretstore e clustersecretstore**, ExternalSecret referencia SecretStore ou ClusterSecretStore, lê provider remoto e reconcilia o Secret alvo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use SecretStore por aplicação em namespace de staging antes de oferecer store compartilhado. Teste em staging autorizado.

## Limites e trade-offs
Store cluster-wide amplia quais namespaces podem solicitar acesso ao backend. Exceções exigem responsável e prazo.

## Como verificar
Confirme escopo, namespace, service account e namespaces permitidos no recurso ativo. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[external-secrets-mapear-segredo-remoto-para-externalsecret]] — Complementa o tópico com external secrets operator: mapear segredo remoto para externalsecret.

## Fontes
- [External Secrets Operator — Google Secret Manager](https://external-secrets.io/latest/provider/google-secrets-manager/) — guia oficial de provider, autenticação e SecretStore para Google Secret Manager; consultado em 2026-10-04.
- [External Secrets Operator — ClusterSecretStore API](https://github.com/external-secrets/external-secrets/blob/main/docs/api/clustersecretstore.md) — referência oficial de escopo e configuração de ClusterSecretStore; consultado em 2026-10-04.
