---
id: software.testes.tranche14.000819
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://tox.wiki/en/latest/reference/config.html", "https://tox.wiki/en/latest/how-to/usage.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# tox: verificar o artefato instalado e não só o checkout

## Em uma frase
tox pode preparar um pacote do projeto e instalá-lo no ambiente antes de rodar os comandos configurados.

## Por que importa
Testar o artefato evita que imports acidentais do diretório corrente escondam arquivos ausentes na distribuição.

## Como funciona
Configure o modo de pacote e confirme que ambiente executa a instalação produzida; use `skip_install` somente quando a intenção for testar dependências isoladas.

## Exemplo
Um job de empacotamento instala o wheel recém-construído e roda testes a partir de diretório fora da raiz do repositório.

## Limites e trade-offs
Estratégia de instalação muda tempo e exige backend de build funcional; execução editable não testa exatamente o mesmo artefato distribuído.

## Como verificar
Verifique `sys.path`, versão importada e conteúdo instalado em uma execução que separe checkout da virtualenv.

## Conexões
- [[tox-parallel-pytest-temp-isolation]] — Veja também: tox: dar basetemp distinto a cada pytest paralelo.

## Fontes
- [tox — Configuration reference](https://tox.wiki/en/latest/reference/config.html) — lista de ambientes, fatores, TOML, templates e configurações por ambiente; consultado em 2026-10-02.
- [tox — How-to usage](https://tox.wiki/en/latest/how-to/usage.html) — execução sequencial/paralela, seleção por ambiente, logs e diretórios temporários; consultado em 2026-10-02.
