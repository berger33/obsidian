---
id: software.seguranca.tranche08.000772
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
fontes: ["https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md", "https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown", "https://github.com/robertdavidgraham/masscan"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Masscan **`--banners`**: Como Resolver o Conflito de **Pacotes `RST` do Kernel Linux** usando **`--source-ip` Dedicado** ou **`--adapter-port` + `iptables`/`nftables`**

## Em uma frase
Diferente de scanners puramente *stateless* de pacote único (que param no `SYN-ACK`), o Masscan possui uma **pilha TCP própria em espaço de usuário** capaz de completar o *three-way handshake* TCP e extrair **Banners de Aplicação (`--banners`)** de HTTP, certificados SSL/TLS X.509, SSH, FTP, SMTP, SMB, RDP, VNC e Memcached!

## Por que importa
Porém, como explica com destaque o `README.md` e o manual `doc/masscan.8.markdown`, existe uma **armadilha clássica quando se usa `--banners`**: como o Masscan envia o pacote `SYN` diretamente pela placa de rede fazendo bypass do kernel, quando o servidor alvo responde com `SYN-ACK` para o IP da sua máquina, **o kernel Linux/Windows da sua máquina vê um `SYN-ACK` de uma conexão que o kernel não abriu e envia imediatamente um pacote `TCP RST` (Reset) matando a conexão antes que o Masscan consiga ler o banner**!

## Como funciona
A documentação oficial do Masscan fornece duas soluções exatas para impedir que o kernel local envie `RST` durante `--banners`: **(Método 1 — Mais limpo)** passar **`--source-ip <IP_DEDICADO_NAO_USADO_PELO_SO>`** na mesma sub-rede LAN (ex.: `192.168.1.222`); ou **(Método 2 — Quando só há 1 IP, como em Wi-Fi/VPS)** fixar a faixa de portas de origem do Masscan com **`--adapter-port 60000-60063`** e bloquear o kernel naquela faixa via `iptables`/`nftables`!

## Exemplo
```bash
# Impedir o kernel Linux de enviar TCP RST na porta de origem 61000 e rodar o Masscan com --banners nessa porta!
sudo iptables -I INPUT -p tcp --dport 61000 -j DROP
sudo masscan 10.10.0.0/16 -p22,80,443,445,3389 \
  --banners \
  --adapter-port 61000 \
  --rate 2000 \
  -oJ /cases/easm/masscan_banners.json
```

## Limites e trade-offs
Lembre-se de remover a regra temporária do `iptables` (`sudo iptables -D INPUT -p tcp --dport 61000 -j DROP`) ao término da varredura, ou utilize o método **`--source-ip`** com um endereço IP livre dedicado da sub-rede local, que não exige nenhuma regra de firewall no host.

## Como verificar
Inspecione no arquivo `/cases/easm/masscan_banners.json` os objetos `"proto": "banner"` e os certificados TLS X.509 decodificados em `"proto": "x509"`.

## Conexões
- [[masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies]] — Veja também: **Masscan (`robertdavidgraham/masscan`)**: Arquitetura Assíncrona *Stateless*, Pilha TCP/IP em User-Space, **Cifra BlackRock** e *SYN Cookies*.
- [[masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede]] — Veja também: Masscan: Dimensionamento de Taxa (`--rate`), Exclusão Obrigatória de Sub-redes Críticas (**`--excludefile`**) e Aceleração **`PF_RING` DNA**.
- [[masscan-customizacao-http-sni-vhost-payloads-heartbleed-poodle]] — Referência cruzada direta com masscan-customizacao-http-sni-vhost-payloads-heartbleed-poodle.

## Fontes
- [Masscan Official GitHub — Mass IP Port Scanner Architecture & Banner Checking](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md) — documentação oficial do Masscan cobrindo transmissão assíncrona, cifra BlackRock, captura de banners, prevenção de TCP RST e PF_RING; consultado em 2026-10-03.
- [Masscan Official Manual Page — masscan(8) Complete CLI & Configuration Reference](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown) — manual oficial masscan(8) cobrindo taxas, excludefile, paused.conf, shards, formatos binários/JSON/XML e payloads UDP/HTTP; consultado em 2026-10-03.
- [Masscan Project Repository — robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) — repositório oficial do código-fonte do Masscan; consultado em 2026-10-03.
