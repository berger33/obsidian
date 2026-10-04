---
id: software.testes.tranche23.001688
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/approvals/ApprovalTests.Java/blob/master/README.md", "https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Approval testing como ponte para legado e dogfood

## Em uma frase
O README enumera "Getting Legacy Code under tests" entre os usos empacotados e, na seção Examples, registra a filosofia: "ApprovalTests eats its own dogfood" — os melhores exemplos da biblioteca estão no próprio código-fonte do repositório.

## Por que importa
Colocar código legado sob teste é o problema em que expectativas escritas à mão mais custam: não há documentação confiável do comportamento atual, que é justamente o que uma verificação por aprovação congela sem julgamento prévio.

## Como funciona
O ciclo sugerido pela combinação das duas seções: verificar a saída atual do código legado (verify num relatório, log, coleção), aprovar o que o sistema hoje faz de fato — inclusive o que deveria ser bug — e então refatorar mantendo os arquivos aprovados como âncora de regressão.

## Exemplo
O material de aprendizado complementa: a seção Learning aponta os Koans como trilha interativa para iniciantes, e há video tutorials de getting started; os podcasts listados incluem gravações do lado .NET.

## Limites e trade-offs
O README não descreve um processo completo de characterization testing — a associação com legado é o uso declarado nos bullets; a disciplina de registrar bugs conhecidos como aprovados cabe à equipe, e a doc do projeto não a padroniza.

## Como verificar
Abra o bullet de legacy code na seção What can it be used for e as seções Examples e Learning do README oficial.

## Conexões
- [[approvaltests-java-fitness]] — Veja também: Compatibilidade Java: JUnit 3/4/5, TestNG e JDK 8+.
- [[approvaltests-no-checked-exceptions]] — Veja também: Filosofia sem exceções checked e API de runtime apenas.

## Fontes
- [ApprovalTests.Java — README oficial](https://github.com/approvals/ApprovalTests.Java/blob/master/README.md) — proposta, compatibilidades, exemplo verifyAll, artefatos aprovados e licença; consultado em 2026-10-03.
- [ApprovalTests — tutorial Getting Started](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md) — verify, verifyAll, JSON, AWT, combinações, aprovação e reporters; consultado em 2026-10-03.
