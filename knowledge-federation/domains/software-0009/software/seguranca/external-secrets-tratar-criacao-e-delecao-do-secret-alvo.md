---
id: software.seguranca.tranche19.001886
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

# External Secrets Operator: Tratar criação e deleção do Secret alvo

## Em uma frase
**External Secrets Operator — Tratar criação e deleção do Secret alvo:** Políticas de criação e deleção determinam como operador lida com Secret manual ou ExternalSecret removido.

## Por que importa
O recorte de **tratar criação e deleção do secret alvo** ajuda a reduzir duplicação manual de credenciais e separar fonte de segredo das aplicações consumidoras. A equipe registra risco, evidência e responsável.

## Como funciona
Para **tratar criação e deleção do secret alvo**, ExternalSecret referencia SecretStore ou ClusterSecretStore, lê provider remoto e reconcilia o Secret alvo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Teste remoção do ExternalSecret e observe se Secret gerenciado permanece ou é apagado. Teste em staging autorizado.

## Limites e trade-offs
Comportamento incorreto pode apagar credencial compartilhada ou deixar cópia órfã. Exceções exigem responsável e prazo.

## Como verificar
Documente ownerReference e policy e valide em namespace descartável. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[external-secrets-usar-datafrom-com-escopo-restrito]] — Complementa o tópico com external secrets operator: usar datafrom com escopo restrito.

## Fontes
- [External Secrets Operator — Google Secret Manager](https://external-secrets.io/latest/provider/google-secrets-manager/) — guia oficial de provider, autenticação e SecretStore para Google Secret Manager; consultado em 2026-10-04.
- [External Secrets Operator — ClusterSecretStore API](https://github.com/external-secrets/external-secrets/blob/main/docs/api/clustersecretstore.md) — referência oficial de escopo e configuração de ClusterSecretStore; consultado em 2026-10-04.
