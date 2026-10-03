---
id: software.seguranca.tranche03.000206
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst", "https://raw.githubusercontent.com/zeek/zeek/master/README.md", "https://github.com/zeek/zeek"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Zeek Intelligence Framework (`intel.log`): ingestão em tempo real de Indicadores de Comprometimento (`ADDR`, `DOMAIN`, `URL`, `FILE_HASH`, `CERT_HASH`)

## Em uma frase
O **Intelligence Framework** do Zeek permite carregar listas de **Indicadores de Comprometimento (IoCs)** de feeds de Threat Intelligence (MISP, OpenCTI, STIX/TAXII convertidos para arquivos tabulares `.dat`) e cruzá-los em memória contra cada IP (`Intel::ADDR`), domínio (`Intel::DOMAIN`), URL (`Intel::URL`), e-mail (`Intel::EMAIL`), User-Agent (`Intel::SOFTWARE`), hash de arquivo (`Intel::FILE_HASH`) e certificado (`Intel::CERT_HASH`) observados na rede, gerando hits detalhados em **`intel.log`**!

## Por que importa
Fazer buscas retroativas de 50.000 domínios e hashes de IoCs no SIEM pode ser lento e caro; quando o Zeek avalia os indicadores em streaming no momento da conexão, o alerta em `intel.log` já traz o `uid` exato da sessão e o contexto onde o indicador foi visto (`seen.where`, ex.: `DNS::IN_REQUEST`, `SSL::IN_SERVER_NAME`, `HTTP::IN_HOST_HEADER`).

## Como funciona
Mais importante: como o Intelligence Framework é alimentado pelo **Input Framework** do Zeek, qualquer atualização no arquivo de IoCs em disco é **recarregada automaticamente em memória em tempo de execução** sem precisar reiniciar o Zeek nem perder pacotes!

## Exemplo
```text
# Exemplo de arquivo de indicadores /opt/zeek/share/zeek/site/intel-feeds.dat (separado por TAB):
#fields	indicator	indicator_type	meta.source	meta.desc	meta.do_notice
198.51.100.77	Intel::ADDR	CORP-CERT	Servidor C2 identificado no incidente #402	T
bad-actor-login.example	Intel::DOMAIN	MISP-Feed	Domínio de credential harvesting	T
```

## Limites e trade-offs
Quando a coluna `meta.do_notice` do feed é definida como `T` (com `policy/frameworks/intel/do_notice` carregado), cada hit em `intel.log` também dispara uma notificação no `notice.log`.

## Como verificar
Teste o carregamento de um arquivo `.dat` de inteligência e verifique os registros gerados em `intel.log`.

## Conexões
- [[zeeknsm-notice-framework-alertas-notice-log-action-alarm-hook]] — Veja também: Zeek Notice Framework (`notice.log`): geração de alertas contextuais (`NOTICE`), deduplicação por `suppress_for` e hooks de resposta.
- [[zeeknsm-arquitetura-cluster-zeekctl-manager-logger-proxy-workers]] — Veja também: Zeek Arquitetura de Cluster (`zeekctl` / `node.cfg`): papéis de `Manager`, `Logger`, `Proxy` e `Workers` com `AF_PACKET` e `lb_procs`.

## Fontes
- [Zeek GitHub — README.md (Network Traffic Analysis & Security Monitoring Framework, Key Features, Scripting & Tooling)](https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst) — README oficial do zeek/zeek apresentando o framework de análise semântica de rede, estado de camada de aplicação e linguagem de scripts; consultado em 2026-10-03.
- [Zeek Official Documentation — Architecture (doc/about/architecture.rst: Event Engine, Packet/Session/File Analysis & Script Interpreter)](https://raw.githubusercontent.com/zeek/zeek/master/README.md) — Documentação oficial de arquitetura do Zeek detalhando a separação entre o Event Engine neutro de política e o Script Interpreter; consultado em 2026-10-03.
- [Zeek Network Security Monitor — Official GitHub Repository](https://github.com/zeek/zeek) — Repositório oficial BSD-3-Clause do Zeek; consultado em 2026-10-03.
