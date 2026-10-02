---
id: software.testes.tranche12.000632
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://github.com/postmanlabs/newman/blob/develop/README.md", "https://learning.postman.com/docs/use/send-requests/variables/managing-environments/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Newman: separar environment e globals

## Em uma frase
O CLI recebe arquivos de environment e globals, e variáveis globais têm precedência inferior às variáveis do environment com o mesmo nome.

## Por que importa
Separar defaults compartilhados de valores próprios de cada alvo evita que a configuração de ambiente seja silenciosamente substituída por uma variável global.

## Como funciona
Passe `--environment` para o conjunto específico do alvo e `--globals` apenas para valores realmente comuns; mantenha tokens fora dos arquivos versionados.

## Exemplo
Uma URL de API pode ser global, enquanto a credencial e o nome de tenant são definidos no environment de staging.

## Limites e trade-offs
Exportar ou publicar um environment pode vazar segredo, e colisões de nomes tornam difícil saber qual valor chegou ao request.

## Como verificar
Use valores sentinela distintos para a mesma chave nos dois arquivos e confira o request final sem imprimir credenciais no log.

## Conexões
- [[newman-collection-source-version]] — Veja também: Newman: fixar a origem da collection executada.
- [[newman-iteration-data-csv-json]] — Veja também: Newman: controlar iterações com arquivo de dados.

## Fontes
- [Newman — README e opções](https://github.com/postmanlabs/newman/blob/develop/README.md) — estado de manutenção, CLI, opções, reporters e uso como biblioteca; consultado em 2026-10-02.
- [Postman — Managing environments](https://learning.postman.com/docs/use/send-requests/variables/managing-environments/) — escopo, uso e precedência de variáveis de ambiente; consultado em 2026-10-02.
