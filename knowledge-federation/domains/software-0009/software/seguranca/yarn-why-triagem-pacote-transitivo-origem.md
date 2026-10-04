---
id: software.seguranca.tranche17.001669
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://yarnpkg.com/cli/why", "https://yarnpkg.com/cli/npm/audit#details"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `yarn why` depois do audit: localizar quem introduziu uma dependência transitiva

## Em uma frase
A documentação recomenda consultar a árvore bruta do relatório ou usar `yarn why pacote` para identificar quem depende do pacote vulnerável.

## Por que importa
Uma atualização direta do pacote alertado pode não ser suficiente quando outro componente fixa a versão; a cadeia identifica o owner correto da mudança.

## Como funciona
Use o advisory para identificar pacote e faixa, consulte dependência reversa e atualize o pai ou a política de resolução com testes adequados.

## Exemplo
Um maintainer pode anexar `yarn why` ao ticket para mostrar qual workspace e qual dependência pai introduziram o pacote no lockfile.

```text
yarn why pacote
```

## Limites e trade-offs
A árvore é uma fotografia da resolução atual; mudanças em ranges e workspaces podem alterar o caminho depois do merge.

## Como verificar
Compare a resposta de `yarn why` com o lockfile e repita a consulta depois da atualização proposta.

## Conexões
- [[yarn-npm-audit-ignore-advisory-id-governanca]] — `--ignore` no Yarn: suprimir advisory específico com revisão recorrente.
- [[yarn-audit-registry-relevancia-caminhos-execucao]] — Relevância de advisories no Yarn: cruzar registry, versão e caminho de execução.

## Fontes
- [Yarn — `yarn why`](https://yarnpkg.com/cli/why) — dependências reversas que explicam a presença de um pacote; consultado em 2026-10-04.
- [Yarn — relatório transitivo do audit](https://yarnpkg.com/cli/npm/audit#details) — recomendação de usar `yarn why` ou relatório JSON para localizar a cadeia; consultado em 2026-10-04.
