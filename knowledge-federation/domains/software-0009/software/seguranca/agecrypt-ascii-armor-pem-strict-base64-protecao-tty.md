---
id: software.seguranca.tranche02.000155
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/FiloSottile/age/main/doc/age.1.html", "https://raw.githubusercontent.com/FiloSottile/age/main/README.md", "https://github.com/FiloSottile/age"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `age` ASCII Armor (`-a` / `--armor`): codificação PEM canônica estrita (`AGE ENCRYPTED FILE`) e proteção de TTY

## Em uma frase
A flag **`-a` / `--armor`** instrui o `age` a codificar a saída cifrada em formato textual ASCII (**`-----BEGIN AGE ENCRYPTED FILE-----`**), utilizando uma versão estrita e canônica de PEM / Base64 sem cabeçalhos extras e sem permitir dados arbitrários antes ou depois do bloco.

## Por que importa
Em sistemas de criptografia legados, codificações Base64 permissivas aceitavam caracteres ignorados ou *trailing data* fora do bloco autenticado, abrindo espaço para confusão de parsers entre ferramentas.

## Como funciona
No `age`, conforme detalhado na man page `age(1)`: 1) se você tentar cifrar sem `-a` e a saída padrão (`stdout`) for um terminal interativo (**TTY**), o `age` **recusa-se a despejar bytes binários no terminal**; 2) com `-a`, o texto ASCII pode ser colado com segurança em issues, e-mails, ConfigMaps ou variáveis; e 3) na descriptografia (`age -d`), o `age` detecta e decodifica o ASCII armor de forma 100% transparente sem precisar passar `-a`!

## Exemplo
```bash
# Cifrando uma string sensível para saída ASCII armored (segura para copiar/colar ou salvar em YAML):
echo "segredo-super-confidencial" | age -a -r age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p
```

## Limites e trade-offs
Se por algum motivo em um script de teste você realmente quiser forçar a saída binária para o stdout conectado a um TTY, especifique explicitamente `-o -`.

## Como verificar
Cifre um arquivo pequeno com `age -a -r <pubkey> -o msg.asc msg.txt` e verifique o cabeçalho `-----BEGIN AGE ENCRYPTED FILE-----`.

## Conexões
- [[agecrypt-passphrase-scrypt-protecao-chaves-identidade-em-repouso]] — Veja também: `age` Criptografia por Passphrase (`-p` / `--passphrase` com `scrypt`) e Identidades Protegidas por Senha.
- [[agecrypt-criptografia-simetrica-com-arquivo-identidade-encrypt-i]] — Veja também: `age` Criptografia Simétrica para Arquivo de Identidade (`age --encrypt -i key.txt`): backups sem gerenciar chave pública separada.

## Fontes
- [FiloSottile age GitHub — README.md (Simple Modern File Encryption Tool, Usage, Multiple Recipients, SSH Keys, Plugins & Go Library)](https://raw.githubusercontent.com/FiloSottile/age/main/doc/age.1.html) — README oficial do FiloSottile/age documentando filosofia sem opções de configuração, uso de chaves X25519 e SSH, destinatários múltiplos, plugins de hardware e integração no ecossistema; consultado em 2026-10-03.
- [FiloSottile age Official Man Page — doc/age.1.html (Complete Specification of Flags -e/-d/-r/-R/-p/-a/-i/-j, Passphrase-Protected Identities & Format Overhead)](https://raw.githubusercontent.com/FiloSottile/age/main/README.md) — Man page oficial age(1) detalhando todas as opções de linha de comando, proteção de TTY, formato ASCII Armor estrito, arquivos de destinatários e identidades cifradas; consultado em 2026-10-03.
- [FiloSottile age — Official GitHub Repository](https://github.com/FiloSottile/age) — Repositório oficial BSD-3-Clause do age; consultado em 2026-10-03.
