---
id: software.seguranca.tranche19.001839
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

# Mozilla SOPS: Gerenciar key groups e threshold

## Em uma frase
**Mozilla SOPS — Gerenciar key groups e threshold:** Grupos de recipients podem combinar chaves e threshold de recuperação da data key.

## Por que importa
O recorte de **gerenciar key groups e threshold** ajuda a versionar configuração com valores secretos cifrados, mantendo campos públicos legíveis para revisão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **gerenciar key groups e threshold**, SOPS gera ou recupera data key, cifra valores selecionados e cifra essa chave com recipients configurados. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Configure recuperação de teste com KMS e age separados apenas quando o modelo de custódia exigir. Teste em staging autorizado.

## Limites e trade-offs
Threshold alto pode impedir recuperação operacional; baixo pode reduzir separação de funções. Exceções exigem responsável e prazo.

## Como verificar
Simule combinações suficientes e insuficientes de recipients em cópias descartáveis. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[sops-tratar-exposicao-no-historico-git]] — Complementa o tópico com mozilla sops: tratar exposição no histórico git.

## Fontes
- [SOPS — Reference](https://getsops.io/docs/reference/) — referência oficial de formatos, cifra de valores e configuração por arquivo; consultado em 2026-10-04.
- [SOPS — Advanced usage](https://getsops.io/docs/usage/advanced/) — guia oficial de creation rules, recipients, rotação e uso avançado; consultado em 2026-10-04.
