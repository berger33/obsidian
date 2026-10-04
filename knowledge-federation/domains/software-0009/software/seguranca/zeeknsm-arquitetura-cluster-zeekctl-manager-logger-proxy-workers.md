---
id: software.seguranca.tranche03.000207
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

# Zeek Arquitetura de Cluster (`zeekctl` / `node.cfg`): papéis de `Manager`, `Logger`, `Proxy` e `Workers` com `AF_PACKET` e `lb_procs`

## Em uma frase
Para monitorar links corporativos de **10 Gbps a 100+ Gbps**, o Zeek opera em uma arquitetura de **Cluster multi-processo** gerenciada pelo **`zeekctl`** e definida em `etc/node.cfg`, dividindo o trabalho entre quatro papéis especializados que se comunicam via biblioteca **Broker / ZeroMQ**: **`worker`** (processa pacotes da placa de rede), **`proxy`** (sincroniza estado distribuído em memória entre workers), **`manager`** (coordena configuração e consolida avisos) e **`logger`** (dedicado a gravar todos os logs em disco sem bloquear os workers).

## Por que importa
Como uma única instância de processo do Zeek executa seu loop de eventos de script em uma thread principal, monitorar uma interface de 10 Gbps com um único processo causaria perda de pacotes (`capture_loss.log`); em vez disso, você instancia N processos `worker` na mesma interface balanceados por hash simétrico de fluxo via `AF_PACKET` (`lb_method=af_packet`, `lb_procs=16`)!

## Como funciona
Separar pelo menos um processo **`logger`** dedicado garante que a serialização de I/O de disco de gigabytes de logs JSON nunca atrase o loop de captura de pacotes dos processos `worker`.

## Exemplo
```ini
# Exemplo de /opt/zeek/etc/node.cfg para um sensor NSM de alta velocidade com 8 workers AF_PACKET:
[logger-1]
type=logger
host=127.0.0.1

[manager]
type=manager
host=127.0.0.1

[proxy-1]
type=proxy
host=127.0.0.1

[worker-1]
type=worker
host=127.0.0.1
interface=af_packet::eth1
lb_method=af_packet
lb_procs=8
pin_cpus=2,3,4,5,6,7,8,9
```

## Limites e trade-offs
Monitore diariamente o arquivo **`capture_loss.log`** gerado pelo script `policy/misc/capture-loss`: ele estima a porcentagem de pacotes perdidos pelo sensor observando lacunas de números de sequência TCP (`percent_lost`), devendo permanecer próximo de `0.0`!

## Como verificar
Execute `zeekctl check`, `zeekctl deploy` e `zeekctl status` para validar e operar o cluster.

## Conexões
- [[zeeknsm-intelligence-framework-ioc-matching-ips-domains-hashes-cif]] — Veja também: Zeek Intelligence Framework (`intel.log`): ingestão em tempo real de Indicadores de Comprometimento (`ADDR`, `DOMAIN`, `URL`, `FILE_HASH`, `CERT_HASH`).
- [[zeeknsm-spicy-parser-generator-gramaticas-seguras-protocolos-arquivos]] — Veja também: Zeek `Spicy`: gerador moderno de parsers seguros em C++ para protocolos de rede e formatos de arquivo customizados.

## Fontes
- [Zeek GitHub — README.md (Network Traffic Analysis & Security Monitoring Framework, Key Features, Scripting & Tooling)](https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst) — README oficial do zeek/zeek apresentando o framework de análise semântica de rede, estado de camada de aplicação e linguagem de scripts; consultado em 2026-10-03.
- [Zeek Official Documentation — Architecture (doc/about/architecture.rst: Event Engine, Packet/Session/File Analysis & Script Interpreter)](https://raw.githubusercontent.com/zeek/zeek/master/README.md) — Documentação oficial de arquitetura do Zeek detalhando a separação entre o Event Engine neutro de política e o Script Interpreter; consultado em 2026-10-03.
- [Zeek Network Security Monitor — Official GitHub Repository](https://github.com/zeek/zeek) — Repositório oficial BSD-3-Clause do Zeek; consultado em 2026-10-03.
