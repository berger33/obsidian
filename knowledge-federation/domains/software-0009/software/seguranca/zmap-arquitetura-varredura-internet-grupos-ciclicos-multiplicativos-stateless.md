---
id: software.seguranca.tranche08.000791
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/zmap/zmap/main/README.md", "https://raw.githubusercontent.com/zmap/zgrab2/master/README.md", "https://github.com/zmap/zmap/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# **ZMap (`zmap/zmap`)**: Arquitetura de Varredura *Stateless* de Pacote Único via Permutação em **Grupos Cíclicos Multiplicativos ($\mathbb{Z}_p^*$)**

## Em uma frase
Desenvolvido por pesquisadores da Universidade de Michigan (Zakir Durumeric, J. Alex Halderman et al., licença Apache-2.0), o **ZMap** (`zmap/zmap`) é um scanner de rede modular de pacote único projetado para realizar **pesquisas e auditorias em escala de internet inteira (ou grandes redes corporativas)** a taxas de **1,4 milhão de pacotes/s em 1 Gbps** (varrendo todo o espaço IPv4 em ~45 minutos) até **14,88 milhões de pacotes/s em 10 Gbps** (em < 5 minutos via `PF_RING` ZC / Netmap)!

## Por que importa
Como o ZMap visita cada um dos $2^{32}$ endereços IPv4 em ordem 100% pseudo-aleatória **sem guardar uma lista de 4 bilhões de IPs na memória RAM e sem repetir nenhum IP**? A resposta matemática elegante do artigo original do ZMap (USENIX Security 2013) é a iteração sobre um **Grupo Cíclico Multiplicativo $(\mathbb{Z}_p^*, \times)$** onde $p = 2^{32} + 15$ é um número primo e $g$ é uma raiz primitiva módulo $p$: a recorrência $x_{n+1} = (x_n \cdot g) \pmod p$ percorre todos os inteiros de $1$ a $2^{32}$ exatamente uma vez usando apenas alguns bytes de estado na CPU!

## Como funciona
Ao mesmo tempo, o receptor do ZMap valida os pacotes de resposta sem manter tabela de conexões codificando um MAC/checksum dos metadados nos campos cabeçalho IP/TCP do pacote de sondagem.

## Exemplo
```bash
# Verificar a versao do ZMap, listar os modulos de sondagem (-M) disponiveis e realizar um dry-run (-d) sem transmitir na rede
zmap --version
zmap --list-probe-modules
zmap -p 443 -n 5 --dryrun
```

## Limites e trade-offs
Observe a flag **`--dryrun` (`-d`)**: antes de executar qualquer varredura real com o ZMap, rodar com `--dryrun -n 5` imprime na tela a representação exata dos quadros Ethernet/IP/TCP que seriam enviados pela placa de rede, permitindo validar IPs de origem, MAC do gateway e portas com zero risco!

## Como verificar
Inspecione a lista de módulos de saída disponíveis executando `zmap --list-output-modules`.

## Conexões
- [[zmap-modulos-sondagem-probe-modules-tcp-synscan-icmp-udp-dns]] — Veja também: ZMap **Probe Modules (`-M`)**: Sondagem `tcp_synscan` (padrão), `icmp_echoscan`, `udp`, `dns` e `upnp` com **`--probe-args`**.
- [[zmap-listas-bloqueio-blocklist-allowlist-conformidade-rfc]] — Referência cruzada direta com zmap-listas-bloqueio-blocklist-allowlist-conformidade-rfc.
- [[masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies]] — Referência cruzada direta com masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies.

## Fontes
- [ZMap Official GitHub — Fast Single-Packet Network Scanner Architecture](https://raw.githubusercontent.com/zmap/zmap/main/README.md) — documentação oficial do ZMap cobrindo permutação por grupos cíclicos multiplicativos, módulos de sondagem/saída e controle de banda; consultado em 2026-10-03.
- [ZGrab 2.0 Official GitHub — Modular Application-Layer (L7) Network Scanner](https://raw.githubusercontent.com/zmap/zgrab2/master/README.md) — documentação oficial do ZGrab 2.0 cobrindo os 30 módulos de protocolo de camada 7, encadeamento com o ZMap e modo multiple.ini; consultado em 2026-10-03.
- [ZMap Official Wiki — Probe Modules, Output Filters, Blocklists & Ethical Scanning](https://github.com/zmap/zmap/wiki) — wiki técnica oficial do ZMap sobre listas de bloqueio RFC 1918, filtros de saída, sharding determinístico e boas práticas de varredura ética; consultado em 2026-10-03.
