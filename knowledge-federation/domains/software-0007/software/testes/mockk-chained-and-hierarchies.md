---
id: software.testes.tranche20.001427
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
fontes: ["https://github.com/mockk/mockk/blob/master/README.md", "https://github.com/mockk/mockk"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockK: encadear dublês e hierarquias

## Em uma frase
Dublês podem devolver outros dublês, permitindo representar cadeias de dependências em estruturas complexas.

## Por que importa
Encadear responde a hierarquias de objetos intermediários que retornam colaboradores, comuns em bibliotecas de acesso a dados.

## Como funciona
Configure a cadeia no nível exato usado pelo código, mantenha a hierarquia rasa e prefira extrair a dependência quando a cadeia ficar profunda.

## Exemplo
O construtor de consultas encadeado pode devolver um dublê de construtor que devolve o dublê de resultado.

## Limites e trade-offs
Cadeias profundas indicam acoplamento a detalhes da biblioteca, e qualquer mudança de estrutura quebra a configuração inteira.

## Como verificar
Substitua a cadeia por uma dependência extraída e compare o tamanho e a fragilidade da configuração nos dois formatos.

## Conexões
- [[mockk-relaxed-unit-and-defaults]] — Veja também: MockK: ajustar respostas padrão.
- [[mockk-limits-and-practices]] — Veja também: MockK: reconhecer limites.

## Fontes
- [MockK — README oficial](https://github.com/mockk/mockk/blob/master/README.md) — dublês, relaxamento, verificação, objetos e corrotinas; consultado em 2026-10-03.
- [MockK — repositório oficial](https://github.com/mockk/mockk) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
