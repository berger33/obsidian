---
id: software.seguranca.tranche19.001834
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

# Mozilla SOPS: Delimitar regras por nome de arquivo

## Em uma frase
**Mozilla SOPS — Delimitar regras por nome de arquivo:** Creation rules podem selecionar recipients e comportamento por caminho ou padrão de arquivo.

## Por que importa
O recorte de **delimitar regras por nome de arquivo** ajuda a versionar configuração com valores secretos cifrados, mantendo campos públicos legíveis para revisão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **delimitar regras por nome de arquivo**, SOPS gera ou recupera data key, cifra valores selecionados e cifra essa chave com recipients configurados. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Crie regra específica para `prod/` e outra para `staging/` em diretório de laboratório. Teste em staging autorizado.

## Limites e trade-offs
Regex de caminho sobreposta pode aplicar recipient errado a arquivo de produção. Exceções exigem responsável e prazo.

## Como verificar
Execute encrypt em arquivos de cada ambiente e confira recipients no metadata do SOPS. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[sops-controlar-campos-criptografados]] — Complementa o tópico com mozilla sops: controlar campos criptografados.

## Fontes
- [SOPS — Reference](https://getsops.io/docs/reference/) — referência oficial de formatos, cifra de valores e configuração por arquivo; consultado em 2026-10-04.
- [SOPS — Advanced usage](https://getsops.io/docs/usage/advanced/) — guia oficial de creation rules, recipients, rotação e uso avançado; consultado em 2026-10-04.
