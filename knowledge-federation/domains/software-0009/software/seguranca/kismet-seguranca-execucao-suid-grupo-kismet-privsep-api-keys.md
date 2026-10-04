---
id: software.seguranca.tranche15.001479
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/kismetwireless/kismet/master/README.md", "https://www.kismetwireless.net/docs/readme/intro/kismet/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura de **Privilege Separation (`privsep`)** do Kismet: Por Que o Servidor `kismet` Roda Sem Privilégios de `root` Usando Helpers SUID Restritos ao Grupo `kismet`?

## Em uma frase
Um sniffer de rede sem fio analisa milhões de quadros 802.11 e Bluetooth vindos do ar — qualquer pessoa na rua pode transmitir pacotes malformados para a antena do seu sensor! Se o servidor principal do sniffer (que faz o parsing complexo dos protocolos, gerencia o banco SQLite e serve a interface HTTP) rodasse como **`root`**, um único bug de memória em um parser daria controle `root` imediato do servidor ao atacante!

## Por que importa
É por isso que o **Kismet** foi projetado desde a base com **Separação Estrita de Privilégios (`Privilege Separation`)**: **(1) O processo principal `kismet` roda 100% como um usuário comum não-privilegiado**; e **(2) Apenas os minúsculos binários auxiliares de captura (`kismet_cap_linux_wifi`, `kismet_cap_linux_bluetooth`) possuem permissão `SUID root` (ou Linux Capabilities `CAP_NET_ADMIN,CAP_NET_RAW`) restrita exclusivamente a membros do grupo Unix `kismet` (`chmod 4750`, dono `root:kismet`)**!

## Como funciona
Mesmo dentro do próprio helper `kismet_cap_linux_wifi`, assim que ele abre o socket `nl80211`/`AF_PACKET` na placa de rede, ele **abandona seus privilégios de `root`** antes de começar a ler pacotes do ar!

## Exemplo
```bash
# Verificar as permissoes de separacao de privilegios (root:kismet 4750) nos binarios kismet_cap_* e adicionar o usuario operador ao grupo kismet
ls -l /usr/bin/kismet_cap_* 2>/dev/null || ls -l /usr/local/bin/kismet_cap_* 2>/dev/null || true
usermod -aG kismet operador_soc
```

## Limites e trade-offs
Por que você **NUNCA deve rodar `sudo kismet` como `root`** se você instalou os pacotes oficiais com suporte ao grupo `kismet`? Porque ao adicionar seu usuário ao grupo `kismet` (`usermod -aG kismet operador_soc`), você inicia o `kismet` diretamente como `operador_soc`: o processo servidor principal jamais tem `UID 0`, e apenas invoca o helper `kismet_cap_*` para configurar a interface de rádio!

## Como verificar
Na interface Web/API do Kismet (`kismet_httpd.conf`), caso exponha a porta `2501` além do `127.0.0.1`, habilite sempre **`httpd_ssl=true`** ou publique-a atrás de um Proxy Reverso autenticado (Nginx / Teleport / Authentik).

## Conexões
- [[kismet-filtros-pacotes-privacidade-pcapng-mascaramento-compliance]] — Veja também: Filtros de Captura e Conformidade de Privacidade (**LGPD / GDPR / PCI-DSS**) em WIDS com Kismet: Gravando Apenas Quadros de Gerenciamento (Sem Dados de Usuários!).
- [[kismet-auditoria-pci-dss-varredura-rogue-ap-trimestral-mapeamento-gps]] — Veja também: Conformidade **PCI-DSS Requisito 11.2 (Auditoria Trimestral de Rogue Wireless)** e Mapeamento de Cobertura Física (`GPS` / `KML`) com Kismet.
- [[kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources]] — Referência cruzada direta com kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources.
- [[kismet-sensores-remotos-kismet-cap-arquitetura-distribuida-tls]] — Referência cruzada direta com kismet-sensores-remotos-kismet-cap-arquitetura-distribuida-tls.

## Fontes
- [Kismet Wireless Official GitHub Repository (`kismetwireless/kismet`)](https://raw.githubusercontent.com/kismetwireless/kismet/master/README.md) — repositório oficial do detector passivo de redes e WIDS Kismet cobrindo suporte a Wi-Fi, Bluetooth, Zigbee, RF/SDR, sensores remotos e API REST/WebSockets; consultado em 2026-10-03.
- [Kismet Official Documentation — Introduction & Architecture (`kismetwireless.net/docs/readme/intro/kismet`)](https://www.kismetwireless.net/docs/readme/intro/kismet/) — documentação arquitetural oficial do Kismet detalhando operação passiva sem emissão RF, configuração `kismet_site.conf`, logs unificados `.kismet` (SQLite3) e `.pcapng`; consultado em 2026-10-03.
