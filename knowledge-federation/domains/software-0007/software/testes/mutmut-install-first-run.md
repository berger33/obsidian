---
id: software.testes.tranche21.001521
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/boxed/mutmut", "https://github.com/boxed/mutmut/blob/main/README.rst"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# mutmut: instalar e rodar sem setup

## Em uma frase
pip install mutmut e um mutmut run na raiz do projeto bastam: o mutmut roda o pytest sobre a pasta tests ou test e tenta descobrir sozinho onde fica o código a mutar.

## Por que importa
Ferramenta de testes de mutação morre de adoção quando exige um arquivo de configuração antes do primeiro resultado; a ausência de setup aqui é a tese do projeto.

## Como funciona
Instale no ambiente de desenvolvimento, rode o comando na raiz e leia o resumo de mutantes mortos e sobreviventes ao final.

## Exemplo
O resumo da primeira corrida em um pacote simples mostra quantos mutantes foram testados em poucos minutos.

## Limites e trade-offs
A autodetecção de caminhos falha em layouts fora do comum (mono-repo, src estranho), exigindo configurar paths na primeira iteração.

## Como verificar
Rode sem configuração em um projeto-pilote e confirme que o mutmut localizou a pasta de código e a de testes.

## Conexões
- [[mutmut-what-mutation-tests]] — Veja também: mutmut: medir testes por defeitos injetados.
- [[mutmut-resume-and-retest]] — Veja também: mutmut: interromper, retomar e retestar.

## Fontes
- [mutmut — README oficial](https://github.com/boxed/mutmut) — instalação, browse, configuração e filtros; consultado em 2026-10-03.
- [mutmut — repositório oficial](https://github.com/boxed/mutmut/blob/main/README.rst) — material-fonte do README e das releases; consultado em 2026-10-03.
