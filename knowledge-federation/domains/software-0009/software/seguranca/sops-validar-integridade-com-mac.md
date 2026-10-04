---
id: software.seguranca.tranche19.001836
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

# Mozilla SOPS: Validar integridade com MAC

## Em uma frase
**Mozilla SOPS — Validar integridade com MAC:** SOPS inclui metadado de integridade para detectar alterações em dados cifrados ou não cifrados conforme configuração.

## Por que importa
O recorte de **validar integridade com mac** ajuda a versionar configuração com valores secretos cifrados, mantendo campos públicos legíveis para revisão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **validar integridade com mac**, SOPS gera ou recupera data key, cifra valores selecionados e cifra essa chave com recipients configurados. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Altere um campo do arquivo de teste e confirme que decrypt identifica discrepância de MAC. Teste em staging autorizado.

## Limites e trade-offs
Desativar validação de integridade enfraquece detecção de edição maliciosa. Exceções exigem responsável e prazo.

## Como verificar
Rode decrypt em cópia modificada e preserve o arquivo original para comparação. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[sops-rotacionar-recipients-sem-trocar-conteudo]] — Complementa o tópico com mozilla sops: rotacionar recipients sem trocar conteúdo.

## Fontes
- [SOPS — Reference](https://getsops.io/docs/reference/) — referência oficial de formatos, cifra de valores e configuração por arquivo; consultado em 2026-10-04.
- [SOPS — Advanced usage](https://getsops.io/docs/usage/advanced/) — guia oficial de creation rules, recipients, rotação e uso avançado; consultado em 2026-10-04.
