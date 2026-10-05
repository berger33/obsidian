---
tipo: auditoria-de-links
lote: software-criacao-ia-2000-0004
tranche: 05
data: 2026-10-04
resultado: aprovada-com-limitacao-de-rede
---

# Auditoria de links — lote `software-criacao-ia-2000-0004`, tranche 5

Data: 2026-10-04. Escopo: notas candidatas IDs **401–500**.

## Resultado

- Referências examinadas: **200** (duas fontes por nota), em **110 URLs citadas distintas** quando fragmentos são tratados como parte da referência.
- Esquema: **200/200 HTTPS**; cada referência está associada a uma nota e rotulada com a página/documentação consultada.
- Fontes internas do vault: o gate final em [`note-quality-software-criacao-ia-2000-0004-tranche-05.md`](note-quality-software-criacao-ia-2000-0004-tranche-05.md) resolveu todos os wikilinks: **100/100 notas sem links wiki quebrados**. Depois da reconciliação, uma auditoria local adicional verificou **7.070 links Markdown** em 107 artefatos da tranche (100 notas, relatórios, fila, manifesto e MOC): **0 destinos locais ausentes**.
- Conteúdo: as fontes primárias foram conferidas no registro factual por nota em [`ai-review-software-criacao-ia-2000-0004-tranche-05.md`](ai-review-software-criacao-ia-2000-0004-tranche-05.md). Foram corrigidas ou delimitadas as afirmações que exigiam distinção de endpoint, evento, versão, transporte ou ciclo de vida.

## Disponibilidade externa e limite do ambiente

A tentativa de consultar os 110 URLs por HTTP a partir do shell retornou **15 respostas HTTP 200**. As outras **95 tentativas terminaram com EOF durante o handshake TLS, antes de qualquer resposta HTTP**; portanto, seu status de disponibilidade **não pôde ser determinado por esse probe**. Esse resultado não é classificado como 404 nem como sucesso. Páginas representativas das dez trilhas foram abertas com sucesso no leitor de documentação durante a revisão factual, incluindo Ollama, ComfyUI, Godot, Unity Sentis, OpenAI Realtime, AI SDK, Storybook, Docusaurus, Ink e Unity Addressables.

Assim, esta auditoria confirma HTTPS, especificidade/relação com as notas e resolução dos links internos; ela não afirma que todas as 110 URLs responderam ao probe HTTP do sandbox. A revisão factual registra as fontes efetivamente consultadas e as ressalvas de versão/comportamento. Um probe completo de disponibilidade pode ser repetido fora do ambiente com restrição de egress.

## Verificações reproduzíveis

- Gate final dos 100 arquivos, com `--path` repetido 100 vezes: **100 aprovados**, 100 revisões por IA registradas, 0 pendências e **wikilinks resolvidos: **100/100****.
- JSONs de origem: dez grupos × dez notas; cada nota contém exatamente duas URLs HTTPS específicas.
- Busca de cobertura: inventário por `git ls-files` no diretório do lote e busca no vault inteiro; nenhum slug ou título exato duplicado entre as 100 candidatas e as notas existentes.
