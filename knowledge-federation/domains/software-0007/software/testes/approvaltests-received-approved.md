---
id: software.testes.tranche23.001681
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

# O par .received e .approved é o protocolo do teste

## Em uma frase
O fluxo documentado: ao rodar, o teste gera YourTestClass.yourTestMethod.received.txt (ou png, html etc.) ao lado do teste, e o teste passa quando esse conteúdo coincide com o arquivo .approved correspondente; se os arquivos coincidem, o received é apagado — a presença de um .received no diretório é a falha, materializada.

## Por que importa
Esse desenho dá ao diff uma interface universal: qualquer ferramenta de comparação de texto serve de "asserção" sobre saída complexa, e o estado do diretório de trabalho conta a história do run sem plugin de IDE.

## Como funciona
O tutorial documenta três caminhos para aprovar: renomear o received para approved; rodar o comando move que a falha imprime na linha de comando (e copia para o clipboard); ou usar "use whole file" no diff reporter — "It doesn't matter how you do it", na frase da doc.

## Exemplo
Provoque uma mudança no output verificado, veja o .received aparecer com o diff do comportamento novo, aprove pelo caminho que preferir e confirme que o segundo run apaga o received e passa.

## Limites e trade-offs
A doc prescreve incluir os .approved no versionamento e adverte que git pode alterar line endings; a correção sugerida é a linha "approved binary" no .gitattributes — sem isso, o teste pode falhar por CRLF em outro SO, não por mudança real.

## Como verificar
Abra a seção Approved File Artifacts do README e a seção Approving The Result do tutorial Getting Started e confirme as três formas e a nota de que arquivos coincidentes fazem o received ser apagado.

## Conexões
- [[approvaltests-capturing-human-intelligence]] — Veja também: ApprovalTests: capturar inteligência humana em vez de codar expectativas.
- [[approvaltests-verify-and-verifyall]] — Veja também: verify para o todo, verifyAll para itens rotulados.

## Fontes
- [ApprovalTests.Java — README oficial](https://github.com/approvals/ApprovalTests.Java/blob/master/README.md) — proposta, compatibilidades, exemplo verifyAll, artefatos aprovados e licença; consultado em 2026-10-03.
- [ApprovalTests — tutorial Getting Started](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md) — verify, verifyAll, JSON, AWT, combinações, aprovação e reporters; consultado em 2026-10-03.
