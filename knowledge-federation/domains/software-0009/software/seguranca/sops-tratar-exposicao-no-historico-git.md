---
id: software.seguranca.tranche19.001840
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
fontes: ["https://getsops.io/docs/reference/", "https://getsops.io/docs/usage/advanced/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Mozilla SOPS: Tratar exposição no histórico Git

## Em uma frase
**Mozilla SOPS — Tratar exposição no histórico Git:** Um arquivo cifrado não reverte plaintext que já foi commitado ou publicado em outra revisão.

## Por que importa
O recorte de **tratar exposição no histórico git** ajuda a versionar configuração com valores secretos cifrados, mantendo campos públicos legíveis para revisão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **tratar exposição no histórico git**, SOPS gera ou recupera data key, cifra valores selecionados e cifra essa chave com recipients configurados. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Se segredo real apareceu no histórico, rotacione credencial e avalie remediação do repositório. Teste em staging autorizado.

## Limites e trade-offs
Reescrever Git sem rotacionar secret não invalida cópias externas nem clones existentes. Exceções exigem responsável e prazo.

## Como verificar
Faça secret scan no histórico e confirme revogação com o provedor antes de encerrar incidente. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cert-manager-declarar-certificate-e-secretname]] — Complementa o tópico com cert-manager: declarar certificate e secretname.

## Fontes
- [SOPS — Reference](https://getsops.io/docs/reference/) — referência oficial de formatos, cifra de valores e configuração por arquivo; consultado em 2026-10-04.
- [SOPS — Advanced usage](https://getsops.io/docs/usage/advanced/) — guia oficial de creation rules, recipients, rotação e uso avançado; consultado em 2026-10-04.
