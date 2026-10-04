---
id: software.testes.tranche20.001438
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://github.com/dubzzz/fast-check", "https://www.npmjs.com/package/fast-check"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# fast-check: reconhecer limites

## Em uma frase
Propriedades verificam invariantes gerais sobre dados gerados, sem provar ausência de erro nem cobrir desempenho ou integração real.

## Por que importa
Tratar a suíte de propriedades como prova de correção ignora que os geradores também têm pontos cegos e que o domínio pode ser mal modelado.

## Como funciona
Escolha invariantes que expressem regras do domínio, teste os geradores, e complemente com exemplos específicos e testes de integração.

## Exemplo
A propriedade de reversão de listas não cobre a ordenação estável nem o custo da operação em listas grandes.

## Limites e trade-offs
Geradores restritos demais deixam de explorar a fronteira do domínio, e invariantes fracas passam a valer mesmo com defeitos presentes.

## Como verificar
Altere a implementação para violar a regra do domínio e confirme que a propriedade detecta a violação antes de considerar a cobertura suficiente.

## Conexões
- [[fc-integration-with-runners]] — Veja também: fast-check: integrar com executores de teste.

## Fontes
- [fast-check — repositório oficial](https://github.com/dubzzz/fast-check) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
- [fast-check — Pacote publicado](https://www.npmjs.com/package/fast-check) — versões, documentação de uso e recursos do pacote; consultado em 2026-10-03.
