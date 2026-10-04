---
id: software.seguranca.tranche19.001832
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

# Mozilla SOPS: Selecionar recipients de KMS

## Em uma frase
**Mozilla SOPS — Selecionar recipients de KMS:** Recipients definem quais identidades ou chaves podem recuperar a data key do documento.

## Por que importa
O recorte de **selecionar recipients de kms** ajuda a versionar configuração com valores secretos cifrados, mantendo campos públicos legíveis para revisão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **selecionar recipients de kms**, SOPS gera ou recupera data key, cifra valores selecionados e cifra essa chave com recipients configurados. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Configure key ARN de ambiente de teste e limite decrypt ao job autorizado. Teste em staging autorizado.

## Limites e trade-offs
Role IAM ampla pode permitir descriptografar segredos de vários ambientes. Exceções exigem responsável e prazo.

## Como verificar
Teste principal autorizado e negado sem exibir plaintext nos logs. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[sops-usar-age-recipient-com-cuidado]] — Complementa o tópico com mozilla sops: usar age recipient com cuidado.

## Fontes
- [SOPS — Reference](https://getsops.io/docs/reference/) — referência oficial de formatos, cifra de valores e configuração por arquivo; consultado em 2026-10-04.
- [SOPS — Advanced usage](https://getsops.io/docs/usage/advanced/) — guia oficial de creation rules, recipients, rotação e uso avançado; consultado em 2026-10-04.
