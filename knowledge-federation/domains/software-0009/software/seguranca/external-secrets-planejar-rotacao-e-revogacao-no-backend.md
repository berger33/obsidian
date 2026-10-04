---
id: software.seguranca.tranche19.001890
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

# External Secrets Operator: Planejar rotação e revogação no backend

## Em uma frase
**External Secrets Operator — Planejar rotação e revogação no backend:** Rotacionar valor externo precisa atualizar consumidores e eventualmente invalidar valor antigo no provider.

## Por que importa
O recorte de **planejar rotação e revogação no backend** ajuda a reduzir duplicação manual de credenciais e separar fonte de segredo das aplicações consumidoras. A equipe registra risco, evidência e responsável.

## Como funciona
Para **planejar rotação e revogação no backend**, ExternalSecret referencia SecretStore ou ClusterSecretStore, lê provider remoto e reconcilia o Secret alvo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Rode rotação de credencial canário e observe reload ou restart controlado do workload. Teste em staging autorizado.

## Limites e trade-offs
Sincronizar novo Secret não revoga automaticamente sessões ou conexões estabelecidas. Exceções exigem responsável e prazo.

## Como verificar
Confirme consumo do valor novo, revogue o anterior e teste que sessão antiga perde validade. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cilium-network-policy-selecionar-endpoints-por-identidade]] — Complementa o tópico com cilium network policies: selecionar endpoints por identidade.

## Fontes
- [External Secrets Operator — Google Secret Manager](https://external-secrets.io/latest/provider/google-secrets-manager/) — guia oficial de provider, autenticação e SecretStore para Google Secret Manager; consultado em 2026-10-04.
- [External Secrets Operator — ClusterSecretStore API](https://github.com/external-secrets/external-secrets/blob/main/docs/api/clustersecretstore.md) — referência oficial de escopo e configuração de ClusterSecretStore; consultado em 2026-10-04.
