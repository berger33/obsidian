---
id: software.seguranca.tranche19.001833
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

# Mozilla SOPS: Usar age recipient com cuidado

## Em uma frase
**Mozilla SOPS — Usar age recipient com cuidado:** SOPS pode proteger data key para recipients age configurados em arquivos ou regras de criação.

## Por que importa
O recorte de **usar age recipient com cuidado** ajuda a versionar configuração com valores secretos cifrados, mantendo campos públicos legíveis para revisão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **usar age recipient com cuidado**, SOPS gera ou recupera data key, cifra valores selecionados e cifra essa chave com recipients configurados. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use public recipient para cifrar fixture e guarde private identity fora do repositório. Teste em staging autorizado.

## Limites e trade-offs
Perder todas as chaves privadas pode tornar dados irrecuperáveis; compartilhá-las amplia exposição. Exceções exigem responsável e prazo.

## Como verificar
Verifique que somente a identidade privada prevista consegue descriptografar fixture. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[sops-delimitar-regras-por-nome-de-arquivo]] — Complementa o tópico com mozilla sops: delimitar regras por nome de arquivo.

## Fontes
- [SOPS — Reference](https://getsops.io/docs/reference/) — referência oficial de formatos, cifra de valores e configuração por arquivo; consultado em 2026-10-04.
- [SOPS — Advanced usage](https://getsops.io/docs/usage/advanced/) — guia oficial de creation rules, recipients, rotação e uso avançado; consultado em 2026-10-04.
