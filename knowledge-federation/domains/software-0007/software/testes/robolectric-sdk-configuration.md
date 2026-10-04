---
id: software.testes.tranche20.001440
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
fontes: ["https://robolectric.org/configuring/", "https://robolectric.org/getting-started/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robolectric: escolher a versão de sistema

## Em uma frase
A execução pode declarar a versão do sistema Android em nível de classe, de pacote ou de arquivo de propriedades.

## Por que importa
Fixar a versão testada evita que mudanças de alvo alterem o comportamento da suíte sem que ninguém perceba.

## Como funciona
Declare a versão na anotação da classe ou no arquivo de propriedades e alinhe a escolha com o alvo mínimo suportado.

## Exemplo
Um teste pode rodar na versão mínima suportada e outro na versão mais recente, cobrindo a faixa real de dispositivos.

## Limites e trade-offs
Testar apenas a versão mais recente deixa passar incompatibilidades em versões antigas que parte dos usuários utiliza.

## Como verificar
Execute o mesmo caso em duas versões declaradas e registre as diferenças de comportamento observadas.

## Conexões
- [[robolectric-jvm-tests]] — Veja também: Robolectric: rodar testes Android na JVM.
- [[robolectric-shadows]] — Veja também: Robolectric: substituir serviços com sombras.

## Fontes
- [Robolectric — Configuração](https://robolectric.org/configuring/) — versão de sistema, sombras, propriedades e repositórios; consultado em 2026-10-03.
- [Robolectric — Primeiros passos](https://robolectric.org/getting-started/) — configuração do projeto, executor e ciclo de vida de telas; consultado em 2026-10-03.
