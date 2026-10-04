---
id: software.testes.tranche19.001291
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://docs.docker.com/guides/localstack/", "https://docs.localstack.cloud/getting-started/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# LocalStack: executar com composição de contêineres

## Em uma frase
A composição declara o serviço, a porta de entrada, as variáveis de ambiente e os volumes que trazem os ganchos e o estado persistente.

## Por que importa
Declarar o ambiente em arquivo torna a subida reproduzível e documenta as dependências entre a aplicação e os serviços emulados.

## Como funciona
Fixe a versão da imagem, monte o diretório de ganchos e a pasta de estado, e defina a variável de serviços habilitados.

## Exemplo
O arquivo pode subir o serviço emulado e a aplicação, garantindo a ordem de inicialização entre eles.

## Limites e trade-offs
Usar a etiqueta mais recente sem fixar a versão introduz mudanças inesperadas, e volumes mal montados fazem os ganchos não serem encontrados.

## Como verificar
Derrube o ambiente, suba novamente e confirme que o estado e os recursos preparados reaparecem conforme configurado.

## Conexões
- [[localstack-init-troubleshooting]] — Veja também: LocalStack: diagnosticar ganchos que não executam.
- [[localstack-persistence]] — Veja também: LocalStack: escolher entre estado limpo e persistente.

## Fontes
- [Docker — Guia do LocalStack](https://docs.docker.com/guides/localstack/) — composição de contêineres, variáveis e ganchos montados; consultado em 2026-10-03.
- [LocalStack — Primeiros passos](https://docs.localstack.cloud/getting-started/) — instalação, execução local e visão geral dos serviços emulados; consultado em 2026-10-03.
