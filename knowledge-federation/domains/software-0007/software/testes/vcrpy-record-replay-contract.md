---
id: software.testes.tranche21.001500
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
fontes: ["https://vcrpy.readthedocs.io/en/latest/usage.html", "https://github.com/kevin1024/vcrpy"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# VCR.py: gravar uma vez, repetir sempre

## Em uma frase
O VCR.py grava as interações HTTP reais em um arquivo de cassetete na primeira execução e reproduz as respostas gravadas nas execuções seguintes.

## Por que importa
Um teste de HTTP fica rápido porque nenhum pedido sai, determinístico porque sobrevive a offline e manutenção do serviço, e fiel porque a resposta traz os mesmos cabeçalhos e corpo originais.

## Como funciona
Envolva o trecho de rede com use_cassette apontando um arquivo, rode uma vez contra o serviço verdadeiro e versione o cassette resultante.

## Exemplo
O teste que consulta a página do IANA passa a rodar offline reproduzindo a resposta guardada no próprio repositório.

## Limites e trade-offs
A fidelidade dura enquanto o contrato remoto não mudar; respostas gravadas escondem regressões do serviço vivo até alguém regrava-las.

## Como verificar
Rode o teste de novo sem rede e confirme que ele passa usando exclusivamente o cassette gravado.

## Conexões
- [[vcrpy-context-decorator]] — Veja também: VCR.py: gerenciar contexto ou decorar a função.

## Fontes
- [VCR.py — Usage](https://vcrpy.readthedocs.io/en/latest/usage.html) — contexto, decorator, record modes e integrações de teste; consultado em 2026-10-03.
- [VCR.py — repositório oficial](https://github.com/kevin1024/vcrpy) — código-fonte, releases e changelog do projeto; consultado em 2026-10-03.
