---
id: software.seguranca.tranche19.001837
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

# Mozilla SOPS: Rotacionar recipients sem trocar conteúdo

## Em uma frase
**Mozilla SOPS — Rotacionar recipients sem trocar conteúdo:** Comando de atualização de chaves permite mudar recipients protegendo a data key de documentos existentes.

## Por que importa
O recorte de **rotacionar recipients sem trocar conteúdo** ajuda a versionar configuração com valores secretos cifrados, mantendo campos públicos legíveis para revisão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **rotacionar recipients sem trocar conteúdo**, SOPS gera ou recupera data key, cifra valores selecionados e cifra essa chave com recipients configurados. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Adicione recipient novo, confira sua capacidade e remova recipient antigo em duas etapas revisadas. Teste em staging autorizado.

## Limites e trade-offs
Remover o único recipient funcional antes de testar o substituto pode bloquear recuperação. Exceções exigem responsável e prazo.

## Como verificar
Descriptografe cópia com chave nova e confirme que chave antiga não continua listada após conclusão. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[sops-descriptografar-em-ci-sem-persistir-plaintext]] — Complementa o tópico com mozilla sops: descriptografar em ci sem persistir plaintext.

## Fontes
- [SOPS — Reference](https://getsops.io/docs/reference/) — referência oficial de formatos, cifra de valores e configuração por arquivo; consultado em 2026-10-04.
- [SOPS — Advanced usage](https://getsops.io/docs/usage/advanced/) — guia oficial de creation rules, recipients, rotação e uso avançado; consultado em 2026-10-04.
